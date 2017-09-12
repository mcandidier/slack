from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q

from .models.channel import Channel, ChannelMembers
from .models.company import Company, CompanyMember 
from .models.message import Message
from .permissions import IsCompanyMember, IsChannelMember

from .serializers import (
    ChannelSerializer,
    MessageSerializer,
    CompanySerializer,
    CompanyMemberSerializer,
    ChannelMemberSerializer
)


from . import signals


class CompanyMixin(object):
    """ Company mixins, return list of methods for company.
    """
    def get_active_company(self):
        return int(self.request.session.get('active_company'))

    def get_channel(self):
        name = self.request.query_params.get('channel', None)
        if name is not None:
            return Channel.objects.get(name=name, company__id=self.get_active_company())
        return None


class ChannelViewSet(CompanyMixin, viewsets.ModelViewSet):
    """Channel API 
    """
    queryset = Channel.objects.all().order_by('-date_creatd')
    serializer_class = ChannelSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember)

    def get_queryset(self):
        # return all channels of different companies for the authenticated user
        queryset = self.queryset.filter(company__id=self.get_active_company())
        return queryset.filter(Q(private=False) | Q(private=True))

    def perform_create(self, serializer):
        # create new channel for company
        serializer.save(company=Company.objects.get(id=self.get_active_company()), owner=self.request.user)


class ChannelMembersViewSet(CompanyMixin, viewsets.ModelViewSet):
    """Channel Members API
    """
    queryset = ChannelMembers.objects.all()
    serializer_class = ChannelMemberSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember)

    def get_queryset(self):
        return self.queryset.filter(channel=self.get_channel())


class MessageViewSet(CompanyMixin, viewsets.ModelViewSet):
    """Channel messages API
    """
    queryset =  Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember,)

    def get_queryset(self):
        # filter only the messages for user selected channel and active company 
        return self.queryset.filter(channel=self.get_channel())

    def perform_create(self, serializer):
        channel = Channel.objects.get(name=self.request.data['channel'], company__id=self.get_active_company())
        serializer.save(sender=self.request.user, channel=channel)


class CompanyViewSet(viewsets.ModelViewSet):
    """Company API
    """
    queryset = Company.objects.all().order_by('-date_created')
    serializer_class = CompanySerializer

    def get_queryset(self):
        # show all the companies which he is member
        user_companies = self.request.user.memberships.all().values_list('company__id', flat=True)
        return self.queryset.filter(id__in=user_companies)


class CompanyMemberViewSet(viewsets.ModelViewSet):
    queryset = CompanyMember.objects.all()
    serializer_class = CompanyMemberSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember)

    def get_queryset(self):
        # display all the members for the active company
        company_id = self.request.session.get('active_company')
        return self.queryset.filter(company__id=int(company_id))


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

