# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from team.models import Team


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    id_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return_ = "Phase " + self.id_phase.name + " enviada pelo Team " + self.id_team.name
        return return_


class Premium(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    winners = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name


class Phase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    activities = models.ManyToManyField(Activity)
    awards = models.ManyToManyField(Premium)

    def __str__(self):
        return self.name


class Hackathon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    team_manager = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="manager")
    teams = models.ManyToManyField(Team, through='Participation', related_name="teams")
    phases = models.ManyToManyField(Phase)

    def __str__(self):
        return self.name


class Participation(models.Model):
    id = models.AutoField(primary_key=True)
    id_hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    LEVEL_ASSES = (
        ('P', 'Participant'),
        ('D', 'Disqualified'),
        ('W', 'Winner'),
        {'I', 'Invited'}
    )
    level_asses = models.CharField(max_length=50, choices=LEVEL_ASSES)
    id_team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return_ = "Team " + self.id_team.name + " é " + self.level_asses + " do Hackathon " + self.id_hackathon.name
        return return_
