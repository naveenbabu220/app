from django.shortcuts import render,HttpResponse
from rest_framework import permissions
from .models import Class1,Video,Payment,Sub,UserCourse
from .serializers import Class1Serilizer, VideoSerilizer,PaymentSerilizer,SubSerilizer,UsercourseSerilizer
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from video import serializers
# Create your views here.
def index(request):
    return HttpResponse('bvksjg v fhnwkfh iwuy')

class Listview(APIView):
    
    def get(self, request, format= None):
        video = Video.objects.all()
        serializer = VideoSerilizer(video, many = True)
        return Response(serializer.data)
    def post(self, request,):
        serializer = VideoSerilizer(data = request.data, files = request.FILES)

        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
 


    