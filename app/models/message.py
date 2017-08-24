from django.db import models
from django.contrib.auth.models import User

from .channel import Channel

class Message(models.Model):
	sender = models.ForeignKey(User, related_name='sender')
	channel = models.ForeignKey(Channel)
	content = models.TextField()
	archived = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now=True)
	date_updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}{}'.format(self.sender, self.content)
