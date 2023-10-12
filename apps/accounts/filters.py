import django_filters
from .models import CustomUser

class CustomUserFilter(django_filters.FilterSet):
    min_birthdate = django_filters.DateFilter(field_name="birth_date", lookup_expr='gte')
    max_birthdate = django_filters.DateFilter(field_name="birth_date", lookup_expr='lte')

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'min_birthdate', 'max_birthdate']