from rest_framework import routers
from . import views 

router = routers.DefaultRouter() 

router.register(r'channels', views.ChannelViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'members', views.CompanyMemberViewSet)
router.register(r'channel-members', views.ChannelMembersViewSet)

urlpatterns =  router.urls