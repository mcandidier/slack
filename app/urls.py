from . import views 
from rest_framework_nested import routers
from django.conf.urls import url, include

"""
API endpoint structure.
    /companies
    /companies/{pk}/
    /companies/{company_pk}/channels
    /companies/{company_pk}/channels/{pk}/
    /companies/{company_pk}/channels/{channel_pk}/messages/
    /companies/{company_pk}/channels/{channel_pk}/members/
"""

router = routers.DefaultRouter() 
router.register(r'companies', views.CompanyViewSet, base_name='companies')

company_router = routers.NestedSimpleRouter(router, r'companies', lookup='company')
company_router.register(r'channels', views.ChannelViewSet, base_name='channels')

channel_router = routers.NestedSimpleRouter(company_router, r'channels', lookup='channel')
channel_router.register(r'messages', views.MessageViewSet, base_name='messages')
channel_router.register(r'members', views.ChannelMembersViewSet, base_name='members')


urlpatterns =  [
    url(r'^', include(router.urls)),
    url(r'^', include(company_router.urls)),
    url(r'^', include(channel_router.urls))
]