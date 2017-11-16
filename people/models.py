from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):

    EDITORIAL = "ED"
    EXEC = "EX"
    EVENTS = "EV"
    DESIGN = "DS"
    WEB = "WB"
    TEAM_CHOICES = (
        (EDITORIAL, 'Editorial'),
        (EXEC, 'Exec'),
        (EVENTS, 'Events'),
        (DESIGN, 'Design'),
        (WEB, 'Web'),
    )

    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default=EDITORIAL)

    stat1 = models.IntegerField()
    stat2 = models.IntegerField()
    stat3 = models.IntegerField()
    stat4 = models.IntegerField()
    stat5 = models.IntegerField()
    stat6 = models.IntegerField()

    name = models.CharField(max_length=100)
    bio = models.TextField()
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="people")
    image2 = models.ImageField(upload_to="people")

