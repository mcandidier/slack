from rest_framework import permissions
from .models.company import Company, CompanyMember
from .models.channel import Channel, ChannelMembers

from django.shortcuts import get_object_or_404


class IsCompanyMember(permissions.BasePermission):

    def has_permission(self, request, view):
        active_company = request.session.get('active_company', None)
        if active_company is not None:
            return CompanyMember.objects.filter(member=request.user, company__id=int(active_company))
        return False


class IsChannelMember(permissions.BasePermission):

    def has_permission(self, request, view):
        name = request.query_params.get('channel', None)
        if name is None and request.method == 'POST':
            name = request.data['channel']

        channel = get_object_or_404(Channel, name=name, company__id=int(request.session.get('active_company')))
        if channel.private:
            channel_members_ids = ChannelMembers.objects.filter(channel=channel).values_list('member__id', flat=True)
            if request.user.id in channel_members_ids:
                return True
            return False
        return True