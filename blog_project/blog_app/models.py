from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse


#UserProfileInfo table links to User table
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',default='default_profile.jpg')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

#BlogPost table links to User table
class BlogPost(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    dateTime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'blog_pics', default='default_blog.jpg')
    
    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title
    
    def portfolio_site(self):
        return reverse('blogs')
 


