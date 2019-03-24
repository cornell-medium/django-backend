from django.db import models

class Contributor(models.Model):
    profile_id =  ForeignKey(to=Profile, related_name="profiles", null=True, blank=True)
    project_id =  models.ForeignKey(to=Project, related_name="owner", null=True, blank=True, unique=True) 

    owner = models.BoolField()
    name = models.CharField(max_length=70)
    netid = models.CharField(max_length=70)
