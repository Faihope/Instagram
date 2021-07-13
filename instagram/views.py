from django import forms
from django.contrib.auth.models import User
from django.db.models.fields import json
from django.http import response
from django.shortcuts import render,redirect
from .models import Following, Image, Like,Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as dj_login
from django.urls import reverse
from django.contrib.auth import login as dj_login

from django.contrib.auth.decorators import login_required
from .forms import UpdateuserForm,UpdateprofileForm,ImageForm
# Create your views here.


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
    
    return render(request,'register.html',context)

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

@login_required(login_url='login')
def welcome(request):
    photos=Image.objects.all()
    user=request.user
    
    context= { 'photos':photos,'user':user}
    return render (request,'welcome.html',context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateuserForm(request.POST, instance=request.user)
        p_form = UpdateprofileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UpdateuserForm(instance=request.user)
        p_form = UpdateprofileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)


# def profilepage(username,request):
#     user=User.objects.filter(username)
#     if user:
#     # current_user = request.user
#         profile = Profile.objects.get(user=user)
#         bio=profile.bio
        
#     if request.method == "POST":
#         form=ImageForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance
#             return redirect(reverse("profile.html",{"obj":obj}))
#         else:
#             form=ImageForm()
#         img=Image.objects.all()
#         return render(request,'profile.html', {'img':img,'form':form})
    

    # context={'u_form':u_form,'p_form':p_form,'current_user':current_user,'profile':profile}

    # return render(request,'profile.html',context=context)

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

def follow(request,username):
    obj=Following.objects.all()
    main_user=request.user
    to_follow=User.objects.get(username=username)

    following=Following.objects.filter(user=main_user,followed=to_follow)
    is_following=True  if following else False

    if is_following:
        Following.unfollow(main_user,to_follow)
        is_following=False
    else:
        Following.follow(main_user,to_follow)
        is_following=False
    resp={'following':is_following}
    response=json.dump(resp)
   
    return render(request,'profile.html',response,context_type='application/json',username=username)

