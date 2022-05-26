from django.conf.urls import url
from blog_app import views
from blog_app.views import  BlogListView, BlogDetailView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog_app'

urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout,name='logout'),
    url(r'^create/$', views.Create_Blog , name='create_blog'),
    url(r'^delete_blog/<id>/$', views.delete_blog ,name='delete_blog'),
    url(r'^update_blog/<id>/$', views.update_blog, name='update_blog'),
    url(r'^index/$', views.index,name='index'),
    url(r'^blog_list/$', BlogListView.as_view(), name="blog_list"),
    url(r'^blog_detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="blog_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
