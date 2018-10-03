from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User, through='Member', related_name='members')

    def __str__(self):
        return self.name


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    LEVEL_ASSES = (
        ('U', 'User'),
        ('A', 'Admin'),
        ('I', 'Invited')
    )
    level_asses = models.CharField(max_length=50, choices=LEVEL_ASSES)
    id_team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return_ = "User " + self.id_user.username + " é " + self.level_asses + " do team " + self.id_team.name
        return return_

