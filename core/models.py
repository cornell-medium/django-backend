from django.db import models

class Event(models.Model):
	title = models.CharField(max_length=20)
	image = models.ImageField(upload_to='static/imgs/events')
	location = models.CharField(max_length = 35)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	description = models.TextField()

	def __str__(self):
		return self.title