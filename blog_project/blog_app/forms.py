from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from blog_app.models import UserProfileInfo, BlogPost


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')
    

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

class BlogPost(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ('title', 'content', 'image')
class  LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class New_Blog_Form(forms.ModelForm):
     class Meta:
        model = BlogPost
        fields = ['user', 'title', 'content', 'dateTime', 'image']

class View_Blog_Form(forms.ModelForm):
     class Meta:
        model = BlogPost
        fields = ['user', 'title', 'content', 'dateTime', 'image']
          
          
       # make dateTime is readonly
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["dateTime"].widget.attrs["readonly"] = True





