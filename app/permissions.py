from rest_framework import permissions
from .models.company import Company, CompanyMember

class IsCompanyMember(permissions.BasePermission):

    def has_permission(self, request, view):
        active_company = request.session.get('active_company', None)
        if active_company is not None:
            return CompanyMember.objects.filter(member=request.user, company__id=int(active_company))
        return False