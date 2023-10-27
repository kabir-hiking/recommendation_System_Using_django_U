from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class UserDat(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    # def __str__(self):
    #     return self.name  