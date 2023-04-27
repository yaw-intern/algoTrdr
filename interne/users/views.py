from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def usr_login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            msg = 'Error login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form':form, 'msg':msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def usr_logout(request):
    logout(request)
    return redirect('/login')


def usr_register(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/dashboard')
    else:
        form = UserCreationForm()
        return render(request, "register.html", {'form': form})
    