from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from .filters import ProductFilter
from .models import *
from .serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
    filter_backends = [SearchFilter]
    search_fields = ['store_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['product_name']
    ordering_fields = ['price']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ComboViewSet(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CarItemViewSet(viewsets.ModelViewSet):
    queryset = CarItem.objects.all()
    serializer_class = CarItemSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StoreReviewViewSet(viewsets.ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CourierRatingViewSet(viewsets.ModelViewSet):
    queryset = CourierRating.objects.all()
    serializer_class = CourierRatingSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




