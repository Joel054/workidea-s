from django.urls import path

from competicoes import Views
app_name = 'competicoes'
urlpatterns = [
    path('', Views.dashboard_hackathon, name='dashboard_hackathon'),
    # path('', Views.list_hackathon, name='list_hackathon'),
    path('new', Views.create_hackathon, name='create_hackathon'),
    path('update', Views.update_hackathon, name='update_hackathon'),
    path('get/<slug:hackathon>', Views.get_hackathon, name='get_hackathon'),
    path('participe', Views.participe_hackathon, name='participe_hackathon'),
    path('phase', Views.create_phase, name='create_phase'),
    path('activity/new', Views.new_activity, name='new_activity'),
    path('activity/update', Views.update_activity, name='update_activity'),
    path('phase/get', Views.get_phase, name='get_phase')
]
