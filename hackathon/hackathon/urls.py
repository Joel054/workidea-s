"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from core import Views
from django.contrib.auth import views as auth_views
# from user import views
#from django.contrib.auth.views import login, logout
#from user.forms import UserAdminCreationForm
from django.urls import path, include


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', Views.register, name='register'),
    path('register_commit/', Views.register_commit, name='register_commit'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', Views.index, name='index'),
    url(r'^dashboard/', Views.dashboard, name='dashboard'),
    path('team/', include("Teams.urls"))
]
