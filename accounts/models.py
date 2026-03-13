from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
# Create your models here.

""" class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    

@reciver(post_save, sender= User)
def create_user_profile(sender, instance, created):
    if created:
        Profile.objects.create(user=instance) """
        
    
""" class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True) """