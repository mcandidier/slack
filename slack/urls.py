from django.conf.urls import url, include
from django.contrib import admin
from app.views import CompanyView
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('app.urls', namespace='api')),
    url(r'^config/(?P<company_id>\d+)/$', CompanyView.as_view(), name='config')
]