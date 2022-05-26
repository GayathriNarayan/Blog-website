from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from blog_app.forms import UserForm,UserProfileInfoForm,LoginForm,New_Blog_Form
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from blog_app.models import User,UserProfileInfo,BlogPost
from blog_project.settings import MEDIA_ROOT,MEDIA_URL
from django.urls import reverse
# from django import forms
from django.shortcuts import get_object_or_404

def index(request):
  return render(request,'blog_app/index.html')

# @login_required
# def home(request):
#   return HttpResponseRedirect(reverse('blog_list'))

"""
Class to use inbuilt ListView object to dipslay list  of all Blogs 

"""

class BlogListView(ListView):
  model = BlogPost
  context_object_name = 'posts'
  template_name = "blog_app/blog_list.html"

"""
Class to use inbuilt DetailView object to dipslay detail of particular Blog

"""

class BlogDetailView(DetailView):
  model = BlogPost
  context_object_name = 'post'
  template_name = "blog_app/blog_detail.html"


def signup(request):
  
  registered = False
  
  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    profile_form = UserProfileInfoForm(data=request.POST)
    
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()

      profile = profile_form.save(commit=False)
      profile.user = user
      
      if 'profile_pic' in request.FILES:
        profile.profile_pic = request.FILES['profile_pic']
        
      profile.save()
      
      registered = True

    else:
      print(user_form.errors, profile_form.errors)
  
  else:
    user_form = UserForm()
    profile_form = UserProfileInfoForm()


  return render(request, 'blog_app/signup.html',
                {'user_form':user_form,
                 'profile_form':profile_form,
                 'registered':registered
                })

def user_login(request):
  '''
  Display the login page for the user to login
  If user logged in check if valid user and display the blog
  else display appropriate error message
  '''
  if request.user.is_authenticated:
    return HttpResponseRedirect(reverse('blog_list'))  
        
  form = LoginForm(request.POST or None)
  if request.POST and form.is_valid():
      user = form.login(request)
      if user:
          login(request,user)
          userObj=User.objects.get(username=user.username)
          user_profile_info=UserProfileInfo.objects.filter(user=userObj).first()
          if userObj:
              #Pass user object and user profile info object
            # return render(request,'blog_app/blog_list.html',{
            #                                   'user':user,
            #                                   'user_profile_info':user_profile_info})
            # portfolio_site=""
            # profile_pic=""
            
            # if user_profile_info:
            #   portfolio_site=user_profile_info.portfolio_site
            #   profile_pic=user_profile_info.profile_pic
              
            # return render(request,'blog_app/profile.html',
            #                             {'username':userObj.username,
            #                             'first_name':user.first_name,
            #                             'last_name':user.last_name,
            #                             'email':userObj.email,
            #                             'portfolio_site':portfolio_site,
            #                             'profile_pic':profile_pic,
            #                             'media_root':MEDIA_ROOT,
            #                             'media_url':MEDIA_URL}) 
            return HttpResponseRedirect(reverse('blog_list'))
          
  return render(request,'blog_app/login.html',{'form':form})
  

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))      

@login_required
def create_blog(request):
    form = New_Blog_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog_list'))
    return render(request, 'blog_app/blog_manager.html', {'form':form})

@login_required
def update_blog(request, id):
    formblog= get_object_or_404(BlogPost, id=id)
    form = New_Blog_Form(request.POST or None, instance=formblog)
    if form.is_valid():
       # form.image=request.FILES['image']
        form.save()
        return HttpResponseRedirect(reverse('blog_list'))
    return render(request, 'blog_app/update_blog.html', {'form':form})

@login_required
# delete view for details
def delete_blog(request, id):
    formblog= get_object_or_404(BlogPost, id=id)    
    if request.method=='POST':
        formblog.delete()
        return HttpResponseRedirect(reverse('blog_list'))
    return render(request,  'blog_app/delete_blog.html', {'form':formblog})  