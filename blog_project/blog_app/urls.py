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
    url(r'^create/$', views.create_blog , name='create_blog'),
    url(r'^delete_blog/(?P<id>\d+)/$', views.delete_blog ,name='delete_blog'),
    url(r'^update_blog/(?P<id>\d+)/$', views.update_blog ,name='update_blog'),
    url(r'^index/$', views.index,name='index'),
    url(r'^blog_list/$', BlogListView.as_view(), name="blog_list"),
    url(r'^blog_detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="blog_detail"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^changepass/$', views.pass_change, name='changepass'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
