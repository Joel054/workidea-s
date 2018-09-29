from django.urls import path

from team import views

urlpatterns = [
    path('', views.list_team, name='list_teams'),
    path('new', views.create_team, name='create_team'),
    path('delete', views.delete_team, name='delete_team'),
    path('update', views.update_team, name='update_team'),
    path('get', views.get_team, name='get_team'),
    path('invitation/new', views.new_team_invitation, name='invitation_team'),
    path('invitation/response', views.invitation_response, name='response_invitations_team')
]
