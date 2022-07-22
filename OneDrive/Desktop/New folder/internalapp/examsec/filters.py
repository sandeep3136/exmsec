import django_filters
from .models import *
from django_filters import CharFilter
class FormFilter(django_filters.FilterSet):
    billid = CharFilter(field_name='billid', lookup_expr='icontains')
    class Meta:
        model = StaffDetails
        fields = ['billid']
