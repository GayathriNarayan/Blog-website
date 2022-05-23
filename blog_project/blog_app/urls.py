from django.conf.urls import url
from blog_app import views

urlpatterns = [
    url(r'user_login', views.index, name="user_login"),
]
