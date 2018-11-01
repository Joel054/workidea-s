
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import render, redirect

from competicoes.models import Hackathon, Participation
from .models import Member, Team
from .Team import return_team
from django.http import HttpResponse
import re
import unicodedata


def remover_acentos(palavra):
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    palavra = palavra.replace("*", "CE")
    palavra = palavra.replace("+", "CE")
    palavra = palavra.replace("-", "CE")
    palavra = palavra.replace("~", "CE")
    palavra = palavra.replace(".", "CE")
    palavra = palavra.replace(",", "CE")
    palavra = palavra.replace("'", "CE")
    palavra = palavra.replace("!", "CE")
    palavra = palavra.replace(":", "CE")
    palavra = palavra.replace("@", "CE")
    palavra = palavra.replace(")", "CE")
    palavra = palavra.replace("(", "CE")
    palavra = palavra.replace("{", "CE")
    palavra = palavra.replace("}", "CE")
    palavra = palavra.replace("[", "CE")
    palavra = palavra.replace("]", "CE")
    palavra = palavra.replace('"', "CE")
    palavra = palavra.replace("/", "CE")
    palavra = palavra.replace("#", "CE")
    palavra = palavra.replace("$", "CE")
    palavra = palavra.replace("%", "CE")
    palavra = palavra.replace("&", "CE")
    palavra = palavra.replace("_", "CE")
    palavra = palavra.replace("=", "CE")
    palavra = palavra.replace("?", "CE")
    palavra = palavra.replace(";", "CE")
    palavra = palavra.replace(":", "CE")
    palavra = palavra.replace("<", "CE")
    palavra = palavra.replace(">", "CE")
    palavra = palavra.replace("ª", "CE")
    palavra = palavra.replace("º", "CE")
    palavra = palavra.replace("°", "CE")
    return ''.join((c for c in unicodedata.normalize('NFD', palavra) if unicodedata.category(c) != 'Mn'))


def list_team(request):
    return return_team(request, None)


def create_team(request):
    user = request.user
    name = request.POST['name']
    num = Team.objects.filter(name=name).count()
    description = request.POST['description']
    nome = remover_acentos(name)
    print(nome)
    slug = nome.replace(' ', '')+str(num)
    team = Team(name=name, description=description, slug=slug)
    team.save()
    member = Member(id_user=user, level_asses='Admin', id_team=team)
    member.save()
    return return_team(request, {'new_team_ok': 'Time cadastrado com sucesso!'})


def delete_team(request):
    user = request.user
    id = request.POST.get('id_team')
    team = Team.objects.get(id=int(id))
    authorization = Member.objects.get(id_user=user, id_team=team)
    context = {'delete': 'error'}
    if authorization is not None:
        if authorization.level_asses == 'Admin':
            team.delete()
            context = {'delete': 'Equipe deletada com sucesso!'}
    return return_team(request, context)


def update_team(request):
    user = request.user
    id = request.POST.get('id_team')
    team = Team.objects.get(id=id)
    authorization = Member.objects.get(id_user=user, id_team=team)
    if authorization:
        if authorization.level_asses == 'Admin':
            team.name = request.POST.get("name")
            team.slug = team.name.replace(' ', '') + id
            team.description = request.POST.get("description")
            team.save()
            return get_team(request, team.slug)
    return return_team(request, None)


def get_team(request, team):
    user = request.user
    team = Team.objects.get(slug=team)
    authorization = Member.objects.get(id_user=user, id_team=team)
    if authorization:
        team_manager = Hackathon.objects.filter(team_manager=team)
        participations = Participation.objects.filter(id_team=team)
        hackathons_disponiveis = Hackathon.objects.all()
        hackathons_disp =[]
        for hacks in hackathons_disponiveis:
            part = Participation.objects.filter(id_team=team, id_hackathon=hacks)
            if part:
                a=1
            else:
                if hacks.team_manager != team:
                    hackathons_disp.append(hacks)
        print(participations)
        print(team_manager)
        context = {
            'team': team,
            'level_asses': authorization.level_asses,
            'members_of_team': team.members.all(),
            'hackathons_managing': team_manager,
            'hackathons_participation': participations,
            'hackathons_disponiveis': hackathons_disp}
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
    return get_team(request, member.id_team.slug)
