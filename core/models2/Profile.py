from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=70)
    bio = models.TextField()
    year = models.CharField(max_length = 10)
    major = models.CharField(max_length=100) #some sort of enum thingy?
    college = models.CharField(max_length=100) #some sort of enum thingy?
    grad_date = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=100)

    # contributor = ForeignKey(to=Contributor, related_name="contributors", null=True, blank=True)

def __str__(self):
        return self.name


# class Contributor(models.Model):
#     project = 
#     profile = 
#     owned_proj =
#     name =  #sync with Profile? 

