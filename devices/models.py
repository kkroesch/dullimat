from django.db import models

class Device(models.Model):
	name = models.CharField(max_length=12)
	description = models.CharField(max_length=200)
	host = models.CharField(max_length=100)
	channel = models.IntegerField()
	
	DEVICE_CHOICES = (
		('1', 'On'),
		('0', 'Off'),
	)
	status = models.CharField(max_length=1, choices=DEVICE_CHOICES)
	
	def __unicode__(self):
		return "%s (%s)" % (self.name, self.description)