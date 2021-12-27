from io import StringIO
import json
from pickle import TRUE
from time import time
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils.timezone import now
# Create your models here.


class Employee(models.Model):
    Social_Network = models.CharField(max_length=255)
    Id = models.CharField(max_length=255,primary_key=TRUE)
    Key_word = models.CharField(max_length=255)
    Names = models.CharField(max_length=255,)
    Link_post = models.CharField(max_length=255,)
    post = models.CharField(max_length=255)
    comment = models.CharField( max_length=255)
    device = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    Job_title = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    Note = models.CharField(max_length=255)
    Activate = models.BooleanField(default=False)
class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
