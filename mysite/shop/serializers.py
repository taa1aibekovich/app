from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'last_name', 'first_name']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'description', 'store_image', 'address']


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'store', 'title', 'contact_number']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name', 'description','product_image', 'price']


class ComboSerializers(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['id','combo_name', 'description', 'combo_image', 'price']


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','user']


class CarItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarItem
        fields = ['id','cart', 'combo', 'quantity']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','status', 'delivery_address']


class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['id','courier_status']


class StoreReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = StoreReview
        fields = ['id','text', 'stars']


class CourierRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','rating']
