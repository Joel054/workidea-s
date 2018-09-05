# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Hackathon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    team_manager = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="manager")
    teams = models.ManyToManyField(Team, related_name="teams")

    def __str__(self):
        return self.name


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    type_notification = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Phase(models.Model):
    id = models.AutoField(primary_key=True)
    id_hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Premium(models.Model):
    id = models.AutoField(primary_key=True)
    id_phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserTeam(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    level_asses = models.CharField(max_length=50)

    def __str__(self):
        return_ = "User " + self.id_user.first_name + "   participa do Team " + self.id_team.name
        return return_


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    id_phase = models.ForeignKey(Phase, on_delete=models.CASCADE, related_name="phase")
    id_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")
    awards = models.ManyToManyField(Premium)

    def __str__(self):
        return_ = "Phase " + self.id_phase.name + " enviada pelo Team " + self.id_team.name
        return return_

