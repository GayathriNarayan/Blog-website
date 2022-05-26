from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

# Create your views here.

def index(request):
  return render(request,'blog_app/index.html')

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

