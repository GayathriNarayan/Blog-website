from django.conf.urls import url
from blog_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name='blog_app'

urlpatterns = [

    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout,name='logout'),
    url(r'^index/$', views.index,name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)