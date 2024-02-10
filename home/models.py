from django.db import models
from login.models import WebsiteUser

# Create your models here.


class Event(models.Model):
    organizer = models.ForeignKey(WebsiteUser, null=True, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=128, null=False, default="TITLE")

    place = models.CharField(max_length=256, null=True)
    date = models.DateField(blank=False, null=True)

    guests = models.ManyToManyField(WebsiteUser, related_name="parties", null=True)
    event_picture = models.ImageField(upload_to='avatars', null=True)


class Invitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="invitation")
    sender = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE, related_name="sended_invitation")
    receiver = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE, related_name="receivied_invitation")

    accepted = models.BooleanField(default=False)

