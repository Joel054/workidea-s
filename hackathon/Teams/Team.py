from django.shortcuts import render, redirect
from core.models import Member, Team


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


# request padrão
def return_team(request, context):
    user = request.user
    members = Member.objects.filter(id_user=user)
    append = {'members': members}
    if context is not None:
        context.update(append)
    else:
        context = append
    return render(request, 'teams.html', context)
