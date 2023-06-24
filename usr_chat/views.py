# usr-chat/views.py
from django.shortcuts import render
from .models import Message
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    return render(request, "usr_chat/index.html")

def room(request, room_name):
    #messages = Message.objects.filter()
    return render(request, "usr_chat/room.html", {"room_name": room_name, "msgHistory": Message.objects.filter(roomid=room_name), "usrData":User})

