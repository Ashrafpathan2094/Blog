from http.client import ImproperConnectionState
from pickle import TRUE
import profile
from re import T
from tkinter import CASCADE
from xml.parsers.expat import model
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    author = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    
    