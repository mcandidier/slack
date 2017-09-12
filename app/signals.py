from django.db.models import signals
from django.dispatch import receiver

from app.models.channel import Channel, ChannelMembers
from app.models.company import Company, CompanyMember

@receiver(signals.post_save, sender=Company)
def create_initial_channels(sender, instance, created, **kwargs):
    if created:
        Channel.objects.create(owner=instance.owner, company=instance, name='general')
        CompanyMember.objects.create(company=instance, member=instance.owner)


@receiver(signals.post_save, sender=Channel)
def add_initial_members(sender, instance, created, **kwargs):
    if created and instance.private:
        ChannelMembers.objects.create(channel=instance, member=instance.owner)