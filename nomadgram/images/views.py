#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from nomadgram.notifications import views as notification_views


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:

                image_list.append(image)

        my_images = user.images.all()[:2]

        for image in my_images:

            image_list.append(image)
        
        sorted_list = sorted(
            image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


class LikeImage(APIView):

    def post(self, request, image_id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except models.Like.DoesNotExist:
            
            new_like = models.Like.objects.create(
                creator=user,
                image=found_image
            )

            new_like.save()

            # create notification for like
            notification_views.create_notification(
                user, found_image.creator, 'like', found_image)

        return Response(status=status.HTTP_201_CREATED)


class UnLikeImage(APIView):

    def delete(self, request, image_id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            preexisting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:

            return Response(status=status.HTTP_304_NOT_MODIFIED)


class CommentOnImage(APIView):

    def post(self, request, image_id, format=None):
    
        user = request.user
        
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():
            
            serializer.save(creator=user, image=found_image)
            
            # create notification for comment
            notification_views.create_notification(
                user, found_image.creator, 'comment', found_image, request.data['message'])

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)  
        
        else:
            return Response(data=serializer.error, status=status.HTTP_400_BAD_REQUEST)


class Comment(APIView):

    def delete(self, request, comment_id, format=None):
        
        user = request.user

        try:
            comment = models.Comment.objects.get(id=comment_id, creator=user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Search(APIView):
    # /search/?terms=hello,cat,dog,...
    def get(self, request, format=None):
        #print(request.query_params)
        hashtags = request.query_params.get('hashtags', None)

        if hashtags is not None:
        
            hashtags = hashtags.split(",")
                    
            images = models.Image.objects.filter(tags__name__in=hashtags).distinct()    # in조건 검색
            # images = models.Image.objects.filter(creator__username__icontains='noma') # like조건검색(icontains: insenstive)
            # images = models.Image.objects.filter(creator__username__exact='noma')     # equals검색(iexact: insenstive)
            serializer = serializers.CountImageSerializer(images, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)


class ModerateComments(APIView):

    def delete(self, request, image_id, comment_id, Format=None):

        user = request.user

        # image의 등록자가 request.user이면서 삭제하고자하는 image id에 추가된
        # 댓글(comment) ID가 URL의 ID와 동일한지 비교.
        try:
            comment_to_delete = models.Comment.objects.get(
                id=comment_id, image__id=image_id, image__creator=user)

            comment_to_delete.delete()

        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageDetail(APIView):

    def get(self, request, image_id, format=None):

        user=request.user

        try:
            image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ImageSerializer(image)

        return Response(data=serializer.data, status=status.HTTP_200_OK)