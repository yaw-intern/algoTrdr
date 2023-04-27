from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.usr_login, name='usr_login'),
    path('logout/', views.usr_logout, name='usr_logout'),
    path('register/', views.usr_register, name='usr_register'),
]