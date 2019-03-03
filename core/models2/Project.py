from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    contributor = models.ManyToManyField(Profile, related_name = "contributors") 
    images = models.ManyToManyField(Tag, related_name = "tags") 
    tags = models.ManyToManyField(Image, related_name = "images") 

    def __str__(self):
        return self.name