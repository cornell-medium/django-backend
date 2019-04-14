from django.db import models
from django.contrib.auth.models import User

class Contributor(models.Model):
    profile =  models.ForeignKey(to=Profile, related_name="profiles", null=True, blank=True)
    name = models.CharField(max_length=70)
    netid = models.CharField(max_length=70)

class Image(models.Model):
    name = models.CharField(max_length=70)
    filepath = models.CharField(max_length=150)
    caption = models.TextField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    acc = models.OneToOneField(User)
    name = models.CharField(max_length=70)
    bio = models.TextField()#not sure how exactly to be represented
    year = models.CharField(max_length = 10)
    major = models.CharField(max_length=100) #some sort of enum thingy?
    college = models.CharField(max_length=100) #some sort of enum thingy?
    grad_date = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=100)


    def __str__(self):
        return self.name

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


class Tag(models.Model)
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

