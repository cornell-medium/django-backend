from django.db import models
from profile import Profile
from project import Project

class Contributor(models.Model):
    profile_id = models.ForeignKey(to=Profile, related_name="profiles", null=True, blank=True)
    project_id = models.OneToOneField(to=Project,  related_name="owner", null=True)
    owner = models.BooleanField()
    name = models.CharField(max_length=70)
    netid = models.CharField(max_length=70)
