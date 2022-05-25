from django import forms
from django.contrib.auth.models import User
from blog_app.models import UserProfileInfo, BlogPost


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')
    

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic', 'bio')

class BlogPost(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ('title', 'content', 'image')






