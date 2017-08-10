from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

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
