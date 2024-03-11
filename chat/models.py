from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100000)

class Message(models.Model):
    username = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=100000)
    value = models.CharField(max_length=1000000)