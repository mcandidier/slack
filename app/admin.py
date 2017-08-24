from django.contrib import admin

# Register your models here.
from .models import channel, company, message

admin.site.register(channel.Channel)
admin.site.register(company.Company)
admin.site.register(company.CompanyMember)
admin.site.register(message.Message)