# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render(request, 'show.html')


def dashboard(request):
    return render(request, 'index.html')


def register_commit(request):
    _username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    if confirm_password == password:
        try:
            user = authenticate(username=_username)
            if user:
                return render(request, 'register.html', {'errors': 'Usuario ja existente'})
            else:
                user2 = authenticate(email=email)
                if user2:
                    return render(request, 'register.html', {'errors': 'Email ja cadastrado'})
                else:
                    user = User.objects.create_user(_username, email, password)
                    user.save()
        except User.DoesNotExist:
            user = User.objects.create_user(_username, email, password)
            user.save()
    else:
        return render(request, 'register.html', {'errors': 'As senhas não correspondem'})
    return redirect('../login/')


def register(request):
    return render(request, 'register.html')


