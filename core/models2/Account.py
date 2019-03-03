from django.db import models

class Account(models.Model):
    username =  models.CharField(max_length=100)
    id = models.CharField(max_length=70)

