from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField("Cover (best ratio is 3:2)", upload_to='static/imgs/events')
    location = models.CharField(blank=True, null=True, max_length = 35)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    description = models.TextField()
    facebook = models.CharField("Facebook event url:", blank=True, null=True, max_length=200)

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    content = models.TextField()
