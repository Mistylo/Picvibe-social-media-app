from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    id_user = models.IntegerField()
    profileimg = models.ImageField(
        upload_to='profile_images/',
        default='profile_images/blank-profile-picture-973460_640.png'
    ) 
    bio = models.TextField(blank=True)  
    location = models.CharField(max_length=100, blank=True)  

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images/') 
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_like = models.IntegerField(default=0)

    def _str_(self):
        return self.users

class LikePost(models.Model):

    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def _str_(self):
        return self.username
    
class FollowerCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def _str_(self):
        return self.user   
    
class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} saved {self.post.id}"
