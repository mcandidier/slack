from rest_framework import permissions
from .models.company import Company

class IsCompanyMember(permissions.BasePermission):

    def has_permission(self, request, view):
        active_company = request.session.get('active_company', None)
        if active_company is not None:
            c_id = int(active_company)
            company_ids = request.user.companies.all().values_list('id', flat=True)
            is_member = Company.objects.filter(id__in=company_ids).exists()
            return is_member


