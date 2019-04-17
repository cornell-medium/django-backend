from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    acc = models.OneToOneField(User)
    name = models.CharField(max_length=70)
    bio = models.TextField()#not sure how exactly to be represented
    year = models.CharField(max_length = 10)
    major = models.CharField(max_length=100) #some sort of enum thingy?
    college = models.CharField(max_length=100) #some sort of enum thingy?
    grad_date = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=200)


def __str__(self):
        return self.name

