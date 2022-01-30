from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = "chat/home.html"
    
class IndexView(generic.TemplateView):
    template_name = "chat/index.html"

class RoomView(generic.TemplateView):
    template_name = "chat/room.html"
    room_name: "room_name"


