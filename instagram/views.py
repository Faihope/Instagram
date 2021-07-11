from django import forms
from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UpdateuserForm,UpdateprofileForm
# Create your views here.
@login_required(login_url='login')
def welcome(request):
    photos=Image.objects.all()

    print(photos)
    context= { 'photos':photos}
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
        return redirect('loginpage')
    context={'form':form}
    
    return render(request,'register.html',context)

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=  request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            loginpage(request,user)
            return redirect('welcome')
        else:
            messages.info(request,'Username or password is incorrect')
       
    context={}
    return render(request,'login.html',context)
@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')


def upload(request):
    if request.method == 'POST':

        data=request.POST
        image=request.FILES.get('image')
        photo = Image.objects.create(
            
                image=image
                )
        return redirect('welcome')


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
        return render(request, 'search_pic.html',{"message":message})

