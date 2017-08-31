from django.db import models
from django.contrib.auth.models import User

from .channel import Channel

class CompanyManager(models.Manager):
    def for_company(self, company_id):
        return super(CompanyManager, self).get_queryset().filter(channel__id=int(company_id))


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    channel = models.ForeignKey(Channel)
    content = models.TextField()
    archived = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    objects = CompanyManager() # The default manager.

    def __str__(self):
        return '{}-{}-{}'.format(self.channel.company, self.sender, self.content)


class DirectMessage(models.Model):
    sender = models.ForeignKey(User, related_name='send_messages')
    receiver = models.ForeignKey(User, related_name='messages')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return '{}-{}'.format(sender.sender, self.receiver)
