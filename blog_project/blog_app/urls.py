from django.conf.urls import url
from blog_app import views

app_name='blog_app'

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout,name='logout'),
    #### BLOG PART ##################
    url(r'^create/$', views.Create_Blog , name='create_blog'),
    url(r'^delete_blog/<id>/$', views.delete_blog ,name='delete_blog'),
    url(r'^update_blog/<id>/$', views.update_blog, name='update_blog'),
]
]
