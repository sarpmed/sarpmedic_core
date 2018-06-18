from django.contrib.auth.models import User
from django.db import models

__author__ = 'andrews'

class Biostatistic(models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=20,decimal_places=5,null=True)
    weight = models.DecimalField(max_digits=20,decimal_places=5,null=True)
    blood_pressure = models.DecimalField(max_digits=20,decimal_places=5,null=True)
