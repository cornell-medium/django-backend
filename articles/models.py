from __future__ import unicode_literals
from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField()
    body = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

