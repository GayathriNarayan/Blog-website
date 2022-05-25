
from django.conf.urls import url
# from django.contrib import admin
# from blog_app import views
from . import views

urlpatterns = [

    url('login',views.login_user, name='login'),
    url('logout_user',views.logout_user, name='logout'),
    url('register', views.register, name='register'),
    url('', views.index, name='index'),

    # url(r'user', views.user),
    # url(r'register', views.register),
    # url(r'', views.home),
    
    ]