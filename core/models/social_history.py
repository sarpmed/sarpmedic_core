from django.db import models

__author__ = 'andrews'

class Social_history(models.Model):
    alcohol = models.BooleanField(default=False)
    smoking  = models.BooleanField(default=False)

