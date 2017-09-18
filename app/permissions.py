from rest_framework import permissions
from .models.company import Company, CompanyMember
from .models.channel import Channel, ChannelMembers

from django.shortcuts import get_object_or_404


class IsCompanyMember(permissions.BasePermission):
    """Check if request/current user is allowed to view the selected company
    """
    def has_permission(self, request, view):
        return CompanyMember.objects.filter(member=request.user, company=view.selected_company)


class IsChannelMember(permissions.BasePermission):
    """Check if request user is a member of selected channel within the compnay
    """
    def has_permission(self, request, view):
        channel = view.selected_channel
        if channel.private:
            channel_members_ids = ChannelMembers.objects.filter(channel=channel).values_list('member__id', flat=True)
            if request.user.id in channel_members_ids:
                return True
            return False
        return True