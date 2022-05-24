from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from blog_app.models import User,UserProfileInfo
from blog_project.settings import MEDIA_ROOT,MEDIA_URL
from django.urls import reverse
# Create your views here.

def index(request):
  return render(request,'blog_app/index.html')

def user_login(request):
  '''
  Display the login page for the user to login
  If user logged in check if valid user and display the blog
  else display appropriate error message
  '''
  if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      user=authenticate(username=username,password=password)
      if user:
          if user.is_active:
              login(request,user)
              userObj=User.objects.get(username=username)
              user_profile_info=UserProfileInfo.objects.filter(user=userObj).first()
              if userObj:
                  #Pass user object and user profile info object
                   return render(request,'blog_app/blog_list.html',{
                                                      'user':user,
                                                      'user_profile_info':user_profile_info})
          else:
              return HttpResponse('ACCOUNT NOT ACTIVE')
      else:
          print('Someone tried to login and failed')
          print('User Name: {} and password {}'.format(username,password))
          return HttpResponse('Invalid Login details')
  else:

      return render(request,'blog_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))      