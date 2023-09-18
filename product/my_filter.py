from django_filters import rest_framework as filters
from .models import Product

class PorductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['contains'],
            'price': ['range', 'lte', 'gte']
        }