# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    commitments = models.ForeignKey('Commitment')

class Commitment(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    end_date = models.DateTimeField()
    goal_description = models.TextField()
    goal_target = models.IntegerField()
    subgroups = models.TextField() #TODO: Change type of subgroup field 

class Followup(models.Model):
    create_date = models.DateTimeField(auto_now_add = True)
    description = models.TextField()
    goal_current = models.IntegerField()
    media = models.TextField()
    commitments = models.ForeignKey('Commitment')


class Organization(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    commitments = models.ManyToManyField(Commitment)
    contacts = models.ManyToManyField(Contact)

