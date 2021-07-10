from django import forms
from django.shortcuts import render,redirect
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.

def welcome(request):
    photos=Image.objects.all()
    context= { 'photos':photos}
    return render (request,'welcome.html',context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account for ' + user + ' was created successfully')
        return redirect('login')
    context={'form':form}
    
    return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=  request.POST.get('password')

        user = authenticate(request,username='username',password='password')
        if user is not None:
            login(request,user)
        return redirect(reverse('welcome'))
    context={}
    return render(request,'login.html',context)


def upload(request):
    if request.method == 'POST':

        data=request.POST
        image=request.FILES.get('image')
        photo = Image.objects.create(
            
                image=image
                )
        return redirect('welcome')


    return render(request,'upload.html')

