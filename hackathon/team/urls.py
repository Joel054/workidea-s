from django.urls import path

from team import Views

urlpatterns = [
    path('', Views.list_team, name='list_teams'),
    path('new', Views.create_team, name='create_team'),
    path('delete', Views.delete_team, name='delete_team'),
    path('update', Views.update_team, name='update_team'),
    path('<slug:team>', Views.get_team, name='get_team'),
    path('invitation/new', Views.new_team_invitation, name='invitation_team'),
    path('invitation/response', Views.invitation_response, name='response_invitations_team')
]
