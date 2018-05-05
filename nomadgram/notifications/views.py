from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
# from django.shortcuts import render


# Create your views here.
class Notifications(APIView):

    def get(self, request, format=None):

        user = request.user
        
        notifications = models.Notification.objects.filter(to=user)

        serializer = serializers.NotificationsSerializer(notifications, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


# user 개인의 notification을 다른 사람이 확인하면 안되기 때문에 view를 function으로 생성한다.
def create_notification(creator, to, notification_type, image=None, comment=None):

    notification = models.Notification.objects.create(
        creator=creator, 
        to=to,
        notification_type=notification_type,
        image=image,
        comment=comment
    )

    notification.save()


