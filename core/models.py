from django.db import models
from django.core.urlresolvers import reverse_lazy


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


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy('view_single_photo', kwargs={'photo_id': self.id})

