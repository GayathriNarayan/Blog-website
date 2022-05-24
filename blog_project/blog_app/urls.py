from django.conf.urls import url
from blog_app import views

app_name='blog_app'

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
]