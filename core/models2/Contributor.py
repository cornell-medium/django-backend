from django.db import models

class Contributor(models.Model):
    profile =  ForeignKey(to=Profile, related_name="profiles", null=True, blank=True)
    name = models.CharField(max_length=70)

