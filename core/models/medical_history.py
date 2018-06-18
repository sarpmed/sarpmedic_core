from django.db import models

__author__ = 'andrews'

class Medical_history(models.Model):
    diabetes_mellitus = models.BooleanField(default=False)
    systematic_hypertension  = models.BooleanField(default=False)
    epilepsy = models.BooleanField(default=False)
    others = models.CharField(max_length=300,null=True)


