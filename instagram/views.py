from django import forms
from django.shortcuts import render,redirect
from .models import Image, Like,Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as dj_login
from django.urls import reverse
from django.contrib.auth import login as dj_login

from django.contrib.auth.decorators import login_required
from .forms import UpdateuserForm,UpdateprofileForm,ImageForm
# Create your views here.
@login_required(login_url='login')
def welcome(request):
    photos=Image.objects.all()
    user=request.user
    
    context= { 'photos':photos,'user':user}
    return render (request,'welcome.html',context)


def register(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    form = CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account for ' + user + ' was created successfully')
        return redirect(reverse('loginpage'))
    context={'form':form}
    
    return render(request,'register.html')

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=  request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('welcome'))
        else:
            messages.info(request,'Username or password is incorrect')
       
    context={}
    return render(request,'login.html',context)
@login_required(login_url='login')
def logout(request):
    
    return redirect(reverse('login'))


def upload(request):
    if request.method == 'POST':

        data=request.POST
        image=request.FILES.get('image')
        photo = Image.objects.create(
                image=image,
              
                
                )
        return redirect(reverse('welcome'))


    return render(request,'upload.html')


def profilepage(request):
    current_user = request.user
    profile = Profile.objects.all()
    u_form=UpdateuserForm()
    p_form=UpdateprofileForm()

    context={'u_form':u_form,'p_form':p_form,'current_user':current_user,'profile':profile}

    return render(request,'profile.html',context)

def search_results(request):
    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='login/')
def like(request):
    user=request.user
    if request.method=='POST':
        image_id=request.POST.get('image_id')
        image_obj=Image.objects.get(id=image_id)

        if user in image_obj.liked.all():
            image_obj.liked.remove(user)
        else:
            image_obj.liked.add(user)
        like,created=Like.objects.get_or_create(user=user,image_id=image_id)
        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        like.save()
        return redirect('welcome')

def uploadImage(request):
    if request.method == "POST":

        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
        return redirect('welcome')
    else:
        form=ImageForm()
        img=Image.objects.all()
    return render(request,"index.html",{"form":form})

def viewPhoto(request,pk=int):
    photo=Image.objects.get(id=pk)
    return render(request,'photo.html',{'photo':photo})
