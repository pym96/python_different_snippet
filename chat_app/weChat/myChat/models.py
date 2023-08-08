from email.policy import default
from multiprocessing.sharedctypes import Value
from tkinter.tix import Tree
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length = 1000)

class Message(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now,blank = True)
    user = models.CharField(max_length = 100000)
    room = models.CharField(max_length = 10000)