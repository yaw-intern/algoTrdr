# usr-chat/views.py
from django.shortcuts import render
from .models import Message

def index(request):
    return render(request, "usr_chat/index.html")

def conversations(request):
    return render(request, "usr_chat/all.html")


def room(request, room_name):
    #messages = Message.objects.filter()
    return render(request, "usr_chat/room.html", {"room_name": room_name})

