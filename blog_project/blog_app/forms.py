
from distutils.command.upload import upload
from django import forms
from mini_blog.models import BlogPost
#, UserProfileInfo

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


          
#class New_Comment_Form(forms.Form):
 #   user_name = forms.CharField(max_length=20)
  #  content=forms.CharField(widget=forms.Textarea)
   # dateTime = forms.DateTimeField(auto_now_add=True)

    #def __str__(self):
     #   return self.title + ""+ self.dateTime + self.content
