# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from hackathon.Teams.models import Team
from hackathon.competicoes.models import Hackathon


def form_new_hackathon(request, context):
    if context is not None:
        return render(request, "newHackathon.html", context)

    return render(request, "newHackathon.html")


def create_hackathon(request):
    hackathon = Hackathon()
    hackathon.name = request.GET['name']
    hackathon.description = request.GET['description']
    team_id = request.GET['team_id']
    try:
        hackathon.team_manager = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return form_new_hackathon(request, {'id_invalido': 'id de time inválido'})
    hackathon.save()
    j_hackathon = {'hackathon': hackathon}
    return render(request, 'hackaton.html', j_hackathon)


# me passem os requests que irão precisar e o que pretendem receber