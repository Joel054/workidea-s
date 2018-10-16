# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unicodedata

from django.shortcuts import render, redirect

# Create your views here.
from core.Views import dashboard
from team.models import Team, Member
from competicoes.models import Hackathon

from competicoes.models import Participation

from competicoes.models import Phase

def remover_acentos(palavra):
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return ''.join((c for c in unicodedata.normalize('NFD', palavra) if unicodedata.category(c) != 'Mn'))

def create_hackathon(request):
    hackathon = Hackathon()
    hackathon.name = request.POST.get('name')
    hackathon.description = request.POST.get('description')
    num = Team.objects.filter(name=hackathon.name).count()
    nome = remover_acentos(hackathon.name)
    hackathon.slug = nome.replace(' ', '')+str(num)
    team_id = request.POST.get('team_id')
    try:
        hackathon.team_manager = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return list_hackathon(request, {'id_invalido': 'id de time inválido'})
    hackathon.save()
    return get_hackathon(request, hackathon.slug)


def update_hackathon(request):
    id = request.POST.get('id_hackathon')
    hackathon = Hackathon.objects.get(id=id)
    user = request.user
    member = Member.objects.get(id_team=hackathon.team_manager, id_user=user)
    if member.level_asses == 'A':
        hackathon.name = request.POST.get('name')
        hackathon.description = request.POST.get('description')
        hackathon.save()
    return get_hackathon(request, hackathon.slug)


def get_hackathon(request, hackathon):
    hackathon = Hackathon.objects.get(slug=hackathon)
    context = {
        'hackathon': hackathon,
        'teams_of_hackathon': hackathon.teams.all()}
    return render(request, 'competicoes/index.html', context)


def list_hackathon(request):
    id = request.POST.get('team_id')
    team = Team.objects.get(id=id)
    user = request.user
    member = Member.objects.filter(id_user=user, id_team=team)
    if member:
        hackathons = Hackathon.objects.filter(team_manager=team)
        context = {'hackathons': hackathons}
        return render(request, 'competicoes/index.html', context)
    return dashboard(request)


# Phase
def create_phase(request):
    user = request.user
    id_hackathon = request.POST.get('id_hackathon')
    hackathon = Hackathon.objects.get(id=id_hackathon)
    member = Member.objects.filter(id_user=user, id_team=hackathon.team_manager)
    if member.level_asses == "Admin":
        phase = Phase()
        phase.name = request.POST.get('name')
        phase.description = request.POST.get('description')
        phase.save()
        hackathon.phases.add(phase)
        hackathon.save()


def dashboard_hackathon(request):
    return render(request, 'competicoes/index.html')


def participe_hackathon(request):
    team_slug = request.GET["team_slug"]
    hackathon_slug = request.GET["hackathon_slug"]
    user = request.user
    team = Team.objects.get(slug=team_slug)
    hackathon = Hackathon.objects.get(slug=hackathon_slug)
    if hackathon.team_manager != team:
        part = Participation.objects.filter(id_team=team, id_hackathon=hackathon)
        if part:
            a = 1;
        else:
            participation = Participation(id_team=team, id_hackathon=hackathon, level_asses='Participant')
            participation.save()
            return get_hackathon(request, hackathon.slug)
    return redirect("/team/"+team.slug)

# def new_activity(request):