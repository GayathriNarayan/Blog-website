from django.conf.urls import url
from blog_app import views

app_name='blog_app'

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout,name='logout'),
    #### BLOG PART ##################
    url(r'^create/$', views.Create_Blog , name='Create_Blog'),
    url(r'^delete_Blog/<id>/$', views.delete_Blog ,name='delete_Blog'),
    url(r'^update_Blog/<id>/$', views.update_Blog, name='update_Blog'),
]
]
