from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth.models import User

from .models.channel import Channel, ChannelMembers
from .models.company import Company, CompanyMember 
from .models.message import Message
from .permissions import IsCompanyMember, IsChannelMember
from . import signals

from .serializers import (
    ChannelSerializer,
    MessageSerializer,
    CompanySerializer,
    CompanyMemberSerializer,
    ChannelMemberSerializer
)


class CompanyMixin(object):
    """ Company mixins, return list of methods for company.
    """
    @property
    def selected_company(self):
        company_name = self.kwargs.get('company_name', None)
        if company_name is not None:
            return Company.objects.get(name=company_name)
        return None

    @property
    def selected_channel(self):
        channel_name =  self.kwargs.get('channel_name', None) 
        if channel_name is not None:
            return Channel.objects.get(name=channel_name, company=self.selected_company)
        return None


class CompanyViewSet(CompanyMixin, viewsets.ModelViewSet):
    """Company API
    """
    queryset = Company.objects.all().order_by('-date_created')
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'name'

    def get_queryset(self):
        # show all the companies which he is member
        user_companies = self.request.user.memberships.all().values_list('company__id', flat=True)
        return self.queryset.filter(id__in=user_companies)


class ChannelViewSet(CompanyMixin, viewsets.ModelViewSet):
    """Channel API 
    """
    queryset = Channel.objects.all().order_by('-date_creatd')
    serializer_class = ChannelSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember)
    lookup_field = 'name'


    def get_queryset(self, *args, **kwargs):
        # return all channels of different companies for the authenticated user
        queryset = self.queryset.filter(company=self.selected_company)
        return queryset.filter(Q(private=False) | Q(private=True))

    def perform_create(self, serializer):
        # create new channel for company
        serializer.save(company=self.selected_company, owner=self.request.user)


class ChannelMembersViewSet(CompanyMixin, viewsets.ModelViewSet):
    """Channel Members API
    """
    queryset = ChannelMembers.objects.all()
    serializer_class = ChannelMemberSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember, IsChannelMember)

    def get_queryset(self):
        return self.queryset.filter(channel=self.selected_channel)

    def perform_create(self, serializer):
        # invite member to a channel
        member = get_object_or_404(User, id=self.request.data['member'])
        serializer.save(member=member, channel=self.selected_channel)

    def destroy(self):
        import pdb; pdb.set_trace()


class MessageViewSet(CompanyMixin, viewsets.ModelViewSet):
    """Channel messages API
    """
    queryset =  Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember, IsChannelMember)

    def get_queryset(self):
        # filter only the messages for user selected channel and active company 
        return self.queryset.filter(channel=self.selected_channel)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, channel=self.selected_channel)


class CompanyMemberViewSet(CompanyMixin, viewsets.ModelViewSet):
    queryset = CompanyMember.objects.all()
    serializer_class = CompanyMemberSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember)

    def get_queryset(self):
        # display all the members for the active company
        return self.queryset.filter(company=self.selected_company)


@method_decorator(csrf_exempt, name='dispatch')
class CompanyView(View):

    def get(self, *args, **kwargs):
        active_company =  self.request.session.get('active_company', None)
        if active_company is not None:
            del self.request.session['active_company']
        company = kwargs.get('company_id', None)
        if company is not None:
            self.request.session['active_company'] =  company
        return HttpResponse('ok')

    def post(self, *args, **kwargs):
        try:
            del self.request.session['active_company']
        except KeyError:
            pass
        return HttpResponse('logging out')

