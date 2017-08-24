from django.db import models
from django.contrib.auth.models import User
from .company import Company

class Channel(models.Model):
	company = models.ForeignKey(Company)
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=128)
	description = models.TextField(null=True, blank=True)
	date_creatd = models.DateTimeField(auto_now=True)
	date_updated = models.DateTimeField(auto_now_add=True)
	archived = models.BooleanField(default=False)

	def __str__(self):
		return self.name