# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Activity, Premium, Phase, Notification, Hackathon, Team, Member
from django.contrib import admin

# Register your models here.

admin.site.register(Team)
admin.site.register(Hackathon)
admin.site.register(Notification)
admin.site.register(Phase)
admin.site.register(Premium)
admin.site.register(Activity)
admin.site.register(Member)

