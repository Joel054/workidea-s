
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from core import Views
from .models import Member, Team
from .Team import return_team
from django.http import HttpResponse


def list_team(request):
    return return_team(request, None)


def create_team(request):
    user = request.user
    name = request.POST['name']
    try:
        team_name = Team.objects.get(name=name)
        if team_name is not None:
            return return_team(request, {'new_team_none': 'new team none'})
    except Team.DoesNotExist:
        pass
    description = request.POST['description']
    id = request.POST.get('id_team')
    if id is int:
        team = Team.objects.get(id=int(id))
        authorization = Member.objects.get(id_user=user, id_team=team)
        if authorization is not None:
            if authorization.level_asses == 'Admin':
                team.name = name
                team.description = description
                team.slug = team.name.replace(' ', '')
                team.save()
                return return_team(request, {'update_team_ok': 'update team ok'})
    team = Team(name=name, description=description, slug=name.replace(' ', ''))
    team.save()
    member = Member(id_user=user, level_asses='Admin', id_team=team)
    member.save()
    return return_team(request, {'new_team_ok': 'new team ok'})


def delete_team(request):
    user = request.user
    id = request.POST.get('id_team')
    team = Team.objects.get(id=int(id))
    authorization = Member.objects.get(id_user=user, id_team=team)
    context = {'delete': 'error'}
    if authorization is not None:
        if authorization.level_asses == 'Admin':
            team.delete()
            context = {'delete': 'delete team ok'}
    return return_team(request, context)


def update_team(request):
    user = request.user
    id = request.POST.get('id_team')
    team = Team.objects.get(id=id)
    authorization = Member.objects.get(id_user=user, id_team=team)
    if authorization:
        if authorization.level_asses == 'Admin':
            team.name = request.POST.get("name")
            team.slug = team.name.replace(' ', '')
            team.description = request.POST.get("description")
            team.save()
            return get_team(request, team.slug)
    return return_team(request, None)


def get_team(request, team):
    user = request.user
    team = Team.objects.get(slug=team)
    authorization = Member.objects.get(id_user=user, id_team=team)
    if authorization:
        context = {'team': team, 'level_asses': authorization.level_asses}
        return render(request, 'team.html', context)
    return return_team(request, None)


def new_team_invitation(request):
    context = []
    if request.method == 'POST':
        team = request.POST.get('team')
        user_id = request.POST.get('user_id')
        team = Team.objects.get(id=team)
        us = User.objects.get(id=user_id)
        invitation = Member(id_user=us, level_asses='Invited', id_team=team)
        invitation.save()
        search = request.POST.get('search')

    else:
        team = request.GET.get('team')
        team = Team.objects.get(id=team)
        search = request.GET.get('search')
    result = User.objects.filter(username__contains=search)
    uses = []
    for use in result:
        invited = Member.objects.filter(id_user=use, id_team=team)
        if invited:
            a = 1
        else:
            uses.append(use)
    context = serializers.serialize('json', uses[:10])
    return HttpResponse(context)


def invitation_response(request):
    response = request.GET["response"]   # resposta (S = sim, N=não)
    user = request.user
    member = request.GET['member']
    member = Member.objects.get(id=member)
    if member.id_user == user:
        if member.level_asses == 'Invited':
            if response == 'S':
                member.level_asses = 'U'
                member.save()
            else:
                member.delete()
    return Views.dashboard(request)