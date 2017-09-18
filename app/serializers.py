from rest_framework import serializers

from .models.channel import Channel, ChannelMembers
from .models.company import Company,CompanyMember
from .models.message import Message


class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = '__all__'
		read_only_fields = ('id', 'owner', 'date_creatd', 'date_updated', 'company')


class ChannelMemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChannelMembers
		fields = '__all__'
		read_only_fields = ('id', 'channel',)


class CompanySerializer(serializers.ModelSerializer):
	class Meta: 
		model = Company
		fields = ('id', 'name', 'description', 'date_created',)
		read_only_fields = ('id',)


class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = '__all__'
		read_only_fields = ('id', 'sender', 'channel')


class CompanyMemberSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()

	def get_name(self, obj):
		return obj.member.username

	class Meta:
		model = CompanyMember
		fields = '__all__'
		read_only_fields = ('id', 'member', 'name')

