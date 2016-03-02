from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from AppYouTubeData.models import ChannelAssociation


admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

admin.site.register(ChannelAssociation)
