from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt

def getToken(request):
    appId =  "6118e51eb7bd4630a66bac8cc561d70c"
    appCertificate = "213c65d186674dedb7deb5e0b4850604"
    channelName = request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTimeInSeconds = 3600 * 24 * 365
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithAccount(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token,'uid':uid},safe=False)

class HomeView(generic.TemplateView):
    template_name = "chat/home.html"
    
class IndexView(generic.TemplateView):
    template_name = "chat/index.html"

class RoomView(generic.TemplateView):
    template_name = "chat/room.html"
    room_name: "room_name"

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)
