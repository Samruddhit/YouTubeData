from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

# Create your models here.

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
   if created:
      Token.objects.create(user=instance)

class ChannelData(models.Model):
    user = models.ForeignKey(User)
    channelid = models.TextField(max_length=100, blank=True, null=True)
    channeltitle = models.TextField(max_length=100, blank=True, null=True)
    channeldescription = models.TextField(max_length=1000, blank=True, null=True)
    channelsubscribers = models.BigIntegerField(max_length=10, blank=True, null=True)
    channelviews = models.BigIntegerField(max_length=10, blank=True, null=True)


class ChannelAssociation(models.Model):
    STATUS_CHOICES = (
    ('T', 'True'),
    ('F', 'False'),
    )
    adminid = models.ForeignKey(User, related_name="Admin")
    employeeid = models.ForeignKey(User, related_name="SubEmployee")
    channelid = models.ForeignKey(ChannelData, related_name="ChannelID")
    permission = models.CharField(choices=STATUS_CHOICES, max_length=1)
