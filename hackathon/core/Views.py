# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpRequest
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
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    if confirm_password == password:
        try:
            user = User.objects.get(username=_username)
            print(user)
            if user is not None:
                return render(request, 'register.html', {'errors': 'Usuario ja existente'})

        except User.DoesNotExist:
            user = User.objects.create_user(_username, email, password, first_name=first_name, last_name=last_name)
            user.save()

    else:
        return render(request, 'register.html', {'errors': 'As senhas não correspondem'})
    return redirect('../login/')


def register(request):
    return render(request, 'register.html')


def get_user(request):
    name = request.GET['name']
    users = User.objects.filter(name=name)
    context = {"users": users}
    return HttpRequest(request, context)
