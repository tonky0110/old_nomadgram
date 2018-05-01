#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllImages(APIView):

    # self: 이미정의된 variable self attribute
    # request: client에게 오브젝트를 요청하는 것.
    # format: json, xml등의 타입(여기선 none)
    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)
    
