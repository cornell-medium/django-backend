from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    contributor = models.ManyToManyField(Profile, related_name = "contributors") 
    owner =  models.ForeignKey(to=Profile, related_name="owner", null=True, blank=True, unique=True) 
    external_link = models.CharField(max_length=200)
    images = models.ManyToManyField(Tag, related_name = "tags") 
    tags = models.ManyToManyField(Image, related_name = "images") 

    def __str__(self):
        return self.name