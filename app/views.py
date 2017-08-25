from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models.channel import Channel
from .models.company import Company, CompanyMember 
from .models.message import Message
from .permissions import IsCompanyMember

from .serializers import ChannelSerializer, MessageSerializer, CompanySerializer, CompanyMemberSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all().order_by('-date_creatd')
    serializer_class = ChannelSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember)

    def get_queryset(self):
        # return all channels of different companies for the authenticated user
        user_companies = self.request.user.company_set.all()
        return self.queryset.filter(company__in=user_companies)


class MessageViewSet(viewsets.ModelViewSet):
    queryset =  Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember)

    def get_queryset(self):
        # filter only the messages for user selected channel and active company 
        company_id = self.request.session.get('active_company')
        name = self.request.query_params.get('channel', None)
        if name is not None:
            return self.queryset.filter(channel__name=name, channel__id=company_id)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class CompanyViewSet(viewsets.ModelViewSet):
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

