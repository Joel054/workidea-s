from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core import Views
from .models import Member, Team
from .Team import return_team


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
        name = request.POST['name']
    description = request.POST['description']
    id = request.POST.get('id_team')
    if id is int:
        team = Team.objects.get(id=int(id))
        authorization = Member.objects.get(id_user=user, id_team=team)
        if authorization is not None:
            if authorization.level_asses == 'Admin':
                team.name = name
                team.description = description
                team.save()
                return return_team(request, {'update_team_ok': 'update team ok'})
    team = Team(name=name, description=description)
    team.save()
    member = Member(id_user=user, level_asses='Admin', id_team=team)
    member.save()
    return return_team(request, {'new_team_ok': 'new team ok'})


def delete_team(request):
    user = request.user
    id = request.GET.get('id_team')
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
    id = request.GET.get('id_team')
    team = Team.objects.get(id=int(id))
    authorization = Member.objects.get(id_user=user, id_team=team)
    if authorization is not None:
        if authorization.level_asses == 'Admin':
            context = {'update': team}
            return return_team(request, context)
    return return_team(request, None)


def get_team(request):
    user = request.user
    id = request.GET.get('id_team')
    team = Team.objects.get(id=int(id))
    authorization = Member.objects.get(id_user=user, id_team=team)
    if authorization is not None:
        context = {'team': team}
        return render(request, 'team.html', context)
    return return_team(request, None)


def new_team_invitations(request):
    team = request.GET['team']
    users = request.GET['users']
    team = Team.objects.get(id=team)
    for user in users:
         us = User.objects.get(id=user)
         invitation = Member(id_user=us, level_asses='C', id_team=team)
         invitation.save()
    return render(request, 'teams.html')


def invitation_response(request):
    response = request.GET["response"] # resposta (S = sim, N=não)
    user = request.user
    member = request.GET['member']
    member = Member.objects.get(id=member)
    if member.id_use == user:
        if member.level_asses == 'C':
            if response == 'S':
                member.level_asses = 'U'
                member.save()
            else:
                member.delete()
            Views.dashboard(request)
    Views.dashboard(request)
