from django.db.models import fields
from rest_framework import serializers
from . models import Class1,Video,Payment,Sub,UserCourse

class Class1Serilizer(serializers.ModelSerializer):
    class Meta:
        model = Class1
        fields = "__all__"
class VideoSerilizer(serializers.ModelSerializer):
     class Meta:
        model = Video
        fields = "__all__"
class PaymentSerilizer(serializers.ModelSerializer):
     class Meta:
        model = Payment
        fields = "__all__"
class SubSerilizer(serializers.ModelSerializer):
     class Meta:
        model = Sub
        fields = "__all__"
class UsercourseSerilizer(serializers.ModelSerializer):
     class Meta:
        model = UserCourse
        fields = "__all__"
 
