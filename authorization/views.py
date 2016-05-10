from django.shortcuts import render, redirect
from django.contrib import auth


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/tracker/')


def login(request):
    if request.POST:
        username = request.POST.get('user', '')
        print(username)
        password = request.POST.get('pass', '')
        print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/tracker/')
        return redirect('/tracker/')
