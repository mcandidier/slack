from rest_framework import serializers

from .models.channel import Channel
from .models.company import Company,CompanyMember
from .models.message import Message

class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = '__all__'
		read_only_fields = ('id',)


class CompanySerializer(serializers.ModelSerializer):
	class Meta: 
		model = Company
		fields = ('name', 'description', 'date_created',)
		read_only_fields = ('id',)


class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = '__all__'
		read_only_fields = ('id', 'sender',)


class CompanyMemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = CompanyMember
		fields = '__all__'
		read_only_fields = ('id', 'member',)



