from http.client import ImproperConnectionState
from pickle import TRUE
from re import T
from xml.parsers.expat import model
from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    