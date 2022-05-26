from django.conf.urls import url
from blog_app import views
from blog_app.views import  BlogListView, BlogDetailView


app_name = 'blog_app'

urlpatterns = [
    url(r'^blog_list/$', BlogListView.as_view(), name="blog_list"),
    url(r'^blog_detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="blog_detail"),
    
]
