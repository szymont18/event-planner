from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

class WebsiteUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='avatars', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name='website_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='website_users', blank=True)

    friends = models.ManyToManyField('self', blank=True)
    waiting_friends = models.ManyToManyField('self', blank=True)
