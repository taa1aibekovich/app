from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'store', StoreViewSet, basename='store')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'combo', ComboViewSet, basename='combo')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'carItem', CarItemViewSet, basename='carItem')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'courier', CourierViewSet, basename='courier')
router.register(r'storeReview', StoreReviewViewSet, basename='storeReview')
router.register(r'courierRating', CourierRatingViewSet, basename='courierRating')

urlpatterns = [
    path('', include(router.urls)),
]
