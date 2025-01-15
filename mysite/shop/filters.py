from django_filters import FilterSet
from .models import *


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt'],
        }

class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact'],
        }
