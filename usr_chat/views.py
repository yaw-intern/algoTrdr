# usr-chat/views.py
from django.shortcuts import render
from .models import Message
from django.http import HttpResponse

def index(request):
    return render(request, "usr_chat/index.html")

def room(request, room_name):
    #messages = Message.objects.filter()
    return render(request, "usr_chat/room.html", {"room_name": room_name})

def allchat(request):
    return HttpResponse("<h1>Cunttwat</h1>")