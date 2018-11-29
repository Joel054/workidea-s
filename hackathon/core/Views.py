# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect


# Create your views here.
from team.Team import return_team

from team.Team import return_generic


def index(request):
    return render(request, 'show.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'teams.html')
    return redirect('login')


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
    return render(request, 'login.html', {'sucess': 'Usuário criado com sucesso!'})


def register(request):
    return render(request, 'register.html')


def get_user(request):
    name = request.GET['name']
    users = User.objects.filter(name=name)
    context = {"users": users}
    return HttpRequest(request, context)


def logout_view(request):
    logout(request)
    return redirect("../")


def update_user(request):
    user = request.user
    if request.user.is_authenticated:
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if username != '':
            test_username = User.objects.filter(username=username).exists()
            if test_username:
                return return_generic(request, 'settings.html', {'error': 'Este username já existe, tente novamente!'})
            user.username = username
        if email != '':
            user.email = email
        if first_name != '':
            user.first_name = first_name
        if last_name != '':
            user.last_name = last_name
        user.save()
        return return_team(request, None)
    return redirect("../login/")


def settings(request):
    return return_generic(request, 'settings.html', None)
