
from .models import Member
from django.shortcuts import render

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



