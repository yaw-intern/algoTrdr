from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.usr_login, name='usr_login'),
]