from django.contrib import admin
from .models import Following, Like, Profile,Image

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Following)
