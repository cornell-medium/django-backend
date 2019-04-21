from django.db import models
from tag import Tag
from image import Image


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    external_link = models.CharField(max_length=200)
    
    images = models.ManyToManyField(Tag, related_name = "tags") 
    tags = models.ManyToManyField(Image, related_name = "images") 

    def __str__(self):
        return self.name