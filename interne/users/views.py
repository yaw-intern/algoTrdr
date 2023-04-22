from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 

# Create your views here.
def usr_login(request):
    return render(request,'login.html', {})