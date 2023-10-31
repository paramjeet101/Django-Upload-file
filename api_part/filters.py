import django_filters
from .models import Data
    
class DataFilter(django_filters.FilterSet):
    class Meta:
        model = Data
        fields = ['industry','year_foundation','locality','country','current_emp','total_emp']
