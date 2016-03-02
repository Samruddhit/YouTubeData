from AppYouTubeData.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Sum, Avg

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')


class ChannelDataSerializer(serializers.Serializer):
    channelid = serializers.CharField(max_length=100,allow_blank=True)
    channeltitle = serializers.CharField(max_length=100,allow_blank=True)
    channeldescription = serializers.CharField(max_length=100,allow_blank=True)
    channelsubscribers = serializers.IntegerField(max_value=50)
    channelviews = serializers.IntegerField(max_value=50)