from django_filters.rest_framework import FilterSet
from .models import Watch


class WatchFilter(FilterSet):
    class Meta:
        model = Watch
        fields = {
            'brand': ['exact'],
            'model': ['exact'],
            'price': ['gt', 'lt']
        }
