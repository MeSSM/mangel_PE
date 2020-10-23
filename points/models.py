from django.db import models
from datetime import datetime
from django.utils import timezone

class Balance(models.Model):
    points = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())

class Points_table(models.Model):
    act = models.CharField(max_length=100)
    price = models.IntegerField()

class Reward(models.Model):
    reward = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())

class Request(models.Model):
    request = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())

class best_pic(models.Model):
    link = models.URLField()

class quote(models.Model):
    quote = models.CharField(max_length=300)
