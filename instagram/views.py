from django.shortcuts import render,redirect
from .models import Image

# Create your views here.

def register(request):
    context={}
    return render(request,'register.html',context)

def login(request):
    context={}
    return render(request,'login.html',context)

def welcome(request):
    photos=Image.objects.all()
    context= { 'photos':photos}
    return render (request,'welcome.html',context)

def upload(request):
    if request.method == 'POST':

        data=request.POST
        image=request.FILES.get('image')
        photo = Image.objects.create(
            
                image=image
                )
        return redirect('welcome')


    return render(request,'upload.html')

