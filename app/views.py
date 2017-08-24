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

    def get_queryset(self):
        user_companies = self.request.user.company_set.all()
        return self.queryset.filter(company__in=user_companies)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-date_created')
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, IsCompanyMember)

    def get_queryset(self):
        channel_id = self.request.session.get('active_company', None)
        name = self.request.query_params.get('channel', None)
        if name is not None and channel_id is not None:
            return self.queryset.filter(channel__id=int(channel_id), channel__name=name)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-date_created')
    serializer_class = CompanySerializer

    def get_queryset(self):
        user_companies = self.request.user.companies.all().values_list('id', flat=True)
        return self.queryset.filter(id__in=user_companies)


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


# class CompanyMemberViewSet(viewsets.ModelViewSet):
#     queryset = CompanyMember.objects.all()
#     serializer_class = CompanyMemberSerializer

#     def get_queryset(self):
#         companies = self.queryset.filter(company__in=self.request.user.company_set.all())
#         return companies.distinct('company')


