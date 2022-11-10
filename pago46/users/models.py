from django.db import models
from django.contrib.auth.models import User as DjangoUser
 # Create your models here.

class User(models.Model):
    last_name = models.CharField(max_length=200, unique=True)