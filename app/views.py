from django.shortcuts import render
from rest_framework import viewsets

from .models.channel import Channel
from .models.company import Company, CompanyMember 
from .models.message import Message

from .serializers import ChannelSerializer, MessageSerializer, CompanySerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all().order_by('-date_creatd')
    serializer_class = ChannelSerializer

    def get_queryset(self):
        user_companies = self.request.user.company_set.all()
        return self.queryset.filter(company__in=user_companies)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-date_created')
    serializer_class = MessageSerializer

    def get_queryset(self):
        channel = self.request.query_params.get('channel', None)
        if channel is not None:
            return self.queryset.filter(channel__name=channel)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-date_created')
    serializer_class = CompanySerializer


