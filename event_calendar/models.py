from django.db import models
from login.models import WebsiteUser

# Create your models here.


class Event(models.Model):
    organizer = models.ForeignKey(WebsiteUser, null=True, on_delete=models.SET_NULL)
    place = models.CharField(max_length=256)

    guests = models.ManyToManyField(WebsiteUser, related_name="parties", null=True)
