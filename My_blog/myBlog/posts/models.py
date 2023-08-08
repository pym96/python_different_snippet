from email.policy import default
import imp
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 10000000)
    created_at = models.DateTimeField(default = datetime.now,blank = True)