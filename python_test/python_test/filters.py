import django_filters as filters

from .models import Client


class ClientFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='icontains')
    phone_number = filters.CharFilter(lookup_expr='icontains')
    suburb = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Client
        fields = []
