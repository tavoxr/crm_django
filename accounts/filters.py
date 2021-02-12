import django_filters
from django_filters import DateFilter
from django.forms.widgets import TextInput
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte', widget=TextInput(attrs={'placeholder': 'mm/dd/yyyy'}))
    end_date = DateFilter(field_name= "date_created", lookup_expr='lte', widget=TextInput(attrs={'placeholder': 'mm/dd/yyyy'}))

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
        
