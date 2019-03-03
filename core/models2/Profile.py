from django.db import models

class Profile(models.Model):
    bio = models.TextField()
    year = models.CharField(max_length = 10)
    major = models.CharField(max_length=100) #some sort of enum thingy?
    college = models.CharField(max_length=100) #some sort of enum thingy?
    grad_date = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=100)


def __str__(self):
        return self.name


