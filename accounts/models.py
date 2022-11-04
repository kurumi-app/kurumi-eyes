from django.db import models
from django.contrib.auth.models import User
import string
import random

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(default="avatars/neko.png", upload_to="avatars", blank=True)
    location = models.CharField(max_length=30, blank=True) 

    def __str__(self):
        return self.user.username

def generate_invite_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

class Invites(models.Model):
    invite = models.CharField(max_length=12, default="", unique=True)

    def save(self, *args, **kwargs):
        self.invite = generate_invite_code()
        super(Invites, self).save(*args, **kwargs)

    def __str__(self):
        return self.invite
