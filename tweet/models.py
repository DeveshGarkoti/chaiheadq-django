from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.text)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'