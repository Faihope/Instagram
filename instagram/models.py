from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_pic=models.ImageField(null=False,blank=True)
    bio=models.TextField(max_length=500)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio


class Image(models.Model):
    image=models.ImageField(blank=True,null=False)
    name=models.CharField(max_length=100)
    caption=models.TextField(max_length=400)
    likes=models.IntegerField(default=0)
    comments=models.CharField(max_length=1000)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
   

    def __str__(self):
        return self.name
