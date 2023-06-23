# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("conversations/", views.conversations, name="conversations"),
    path("<str:room_name>/", views.room, name="room"),
]