from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from AppYouTubeData.models import *
from apiclient.discovery import build
from apiclient.errors import HttpError
from YouTubeData.settings import DEVELOPER_KEY, YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from AppYouTubeData.serializers import *
from django.contrib.auth import authenticate, logout, login
from rest_framework import authentication


def Home(request):
    return render(request, 'forms.html')


def Login(request):
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return render(request, 'login.html')


def LoginAuthentication(request):
    if request.method == "POST":
        email = request.POST['emailid']
        password = request.POST['password']
        isUser = User.objects.filter(email=request.POST['emailid'])
        if len(isUser) == 0:
            email = str(email)
            errorMessage = "email address %s is not registered with us" % email
            return render(request,'login.html', {'errorMessage': errorMessage})
        else:
            user = authenticate(username=email, password=password)
            if user:

                login(request, user)
                return render(request, 'forms.html')
            else:
                errorMessage = "Password is invalid"
                return render(request, "login.html", {'errorMessage': errorMessage})

    else:
        return render(request, 'login.html')


@login_required()
def FetchYouTubeData(request):
    if request.method == "POST":

        channelName = request.POST['channelName']

        if channelName == '':
            errorMessage = "Please Enter the Channel Name! It cannot be empty."
            return render(request, 'forms.html', {'errorMessage': errorMessage})

        else:
            youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

            try:
                isValidChannel = youtube.search().list(part="id,snippet",channelId=channelName,).execute()
            except:
                errorMessage = "Please Enter the Valid Channel Name, \"%s\" is not valid channel" %channelName
                return render(request, 'forms.html', {'errorMessage': errorMessage, 'channelName':channelName})

            else:
                channelData = youtube.channels().list(part="id,snippet,statistics",id=channelName,).execute()

                for items in channelData.get("items", []):
                    if channelData.get("items") != []:
                        if items["kind"] == "youtube#channel" and items["id"] == channelName:
                            channelId = items["id"]
                            if items["snippet"]["title"] != "":
                                channelTitle = items["snippet"]["title"]
                            else:
                                channelTitle = "None"

                            if items["snippet"]["description"] != "":
                                channelDescription = items["snippet"]["description"]

                            else:
                                channelDescription = "None"

                            if items["statistics"]["subscriberCount"] != "":
                                channelSubscribersCount = items["statistics"]["subscriberCount"]
                            else:
                                channelSubscribersCount = 0

                            if items["statistics"]["viewCount"] != "":
                                channelViewCount = items["statistics"]["viewCount"]
                            else:
                                channelViewCount = 0
                currentUser = request.user
                channeldata = ChannelData()
                channeldata.user_id = currentUser.id
                channeldata.channelid = channelId
                channeldata.channeltitle = channelTitle
                channeldata.channeldescription = channelDescription
                channeldata.channelsubscribers = channelSubscribersCount
                channeldata.channelviews = channelViewCount
                channeldata.save()
                successMessage = "Data has been fetched and saved to Database Successfully!"
                return render(request, 'forms.html', {'SuccessMessage': successMessage})
    else:
        return render(request, 'forms.html')


@login_required()
def GetDataResult(request):
    #getAllData = ChannelAssociation.objects.filter(employeeid=request.user.id,permission='T')
    getAllData = ChannelData.objects.all()
    return render(request, 'tables.html', {'channelData':getAllData})



class GetChannelData(APIView):
    def get(self, request):
        channelData = ChannelData.objects.all()
        allData = []
        channelDataSerializer = ChannelDataSerializer(channelData,many=True)
        true = {'Response':True}
        allData.extend([true,channelDataSerializer.data])
        return Response(allData)