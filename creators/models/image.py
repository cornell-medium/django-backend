from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=70)
    
    filepath = models.CharField(max_length=150)
    caption = models.TextField()

    def __str__(self):
        return self.name