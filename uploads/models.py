from django.db import models
from django.contrib.auth.models import User
import string
import random
# Create your models here.

def randomizer():
    # create custom password
    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(10))

class ImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = randomizer()
        super(ImageUpload, self).save(*args, **kwargs)