from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(default="avatars/neko.png", upload_to="avatars", blank=True)
    location = models.CharField(max_length=30, blank=True) 

    def __str__(self):
        return self.user.username