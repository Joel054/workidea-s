# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from Teams.models import Team


# Create your models here.


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    type_notification = models.CharField(max_length=255)

    def __str__(self):
        return self.name









