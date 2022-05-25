import email
import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.


def index(request):
  return render(request,'index.html')

def login_user(request):
  if request.method=='POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request,'login successfull')
      return redirect('index.html')
    else:
      messages.success(request,'Invalid credentials, Try again')
      return redirect('login.html')
  return render(request,'login.html')

def logout_user(request):
     logout(request)
     messages.success(request,'Logout Successfully')
     return redirect('home.html')


def register(request):
  if request.method=='POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    username = request.POST.get('username')
    user=User(email=email, password=password, first_name=firstname, last_name=lastname, username=username)
    if User.objects.filter(email=email).exists():
      messages.warning(request,'Email already registered')
      return redirect('register.html')
    else:
      user.save()
      messages.success(request, 'Registered successfully')
      return redirect('/')
  return render(request,'register.html')