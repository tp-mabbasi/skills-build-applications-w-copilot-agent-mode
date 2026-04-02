
from django.db import models
from djongo.models import ObjectIdField


class User(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class Team(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)


class Activity(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()


class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)


class Workout(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.CharField(max_length=100)
