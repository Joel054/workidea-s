# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from team.models import Member, Team

from competicoes.models import Hackathon, Phase, Premium, Activity
from .models import Notification
from django.contrib import admin

# Register your models here.

admin.site.register(Team)
admin.site.register(Hackathon)
admin.site.register(Notification)
admin.site.register(Phase)
admin.site.register(Premium)
admin.site.register(Activity)
admin.site.register(Member)

