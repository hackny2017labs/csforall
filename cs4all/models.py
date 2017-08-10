# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def get_username(self):
        return self.user.username

class Commitment(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    end_date = models.DateTimeField()
    goal_description = models.TextField()
    goal_target = models.IntegerField()
    goal_current = models.IntegerField()
    contacts = models.ManyToManyField(User)

class Organization(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    contacts = models.ManyToManyField(User)

