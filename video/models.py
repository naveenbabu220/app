from django.db import models
# Create your models here.
from django.core.validators import FileExtensionValidator
from django.conf  import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Class1(models.Model):
        class1 = models.CharField(max_length=100,null=False)
        price = models.DecimalField(decimal_places=2, max_digits=5,null=True)
       
        def __str__(self):
                return self.class1

class UserCourse(models.Model):
        user=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
        course=models.ManyToManyField(Class1)
        date = models.DateTimeField(auto_now_add=True)
        datecompltion = models.DateTimeField()


        def __str__(self):
                return f'{self.user.username}'
        
class Payment(models.Model):
    order_id= models.CharField(max_length=50,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_course=models.ForeignKey(UserCourse,null=True,blank=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=50,null = True)
    status = models.BooleanField(default=False)
    course=models.ForeignKey(Class1,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    @property
    def is_active(self):
        return self.status == "active" or self.status == "trialing"
            
class Sub(models.Model):
        sub = models.CharField(max_length=100,default="maths")
        def __str__(self):
                return self.sub


class Video(models.Model):
        caption  = models.CharField(max_length=100)
        video = models.FileField(upload_to="video/%y")
        sub = models.ForeignKey(Sub,on_delete=models.CASCADE)
        class1 = models.ForeignKey(Class1,on_delete=models.CASCADE)
        def __str__(self):
                return self.caption
