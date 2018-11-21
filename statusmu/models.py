from django.db import models
from django.utils import timezone

# Create your models here.


class Statusmu(models.Model):
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=300)   
    date = models.DateTimeField(default=timezone.now)


class User(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
