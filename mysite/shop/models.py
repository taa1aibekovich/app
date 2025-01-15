from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    profile_image = models.ImageField(null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    date_register = models.DateField(auto_now_add=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    STATUS_CHOICES = (
        ('simpleUser', 'simpleUser'),
        ('ownerUser', 'ownerUser'),
        ('curier', 'curier')
    )
    user_status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='simpleUser')

    def __str__(self):
        return f'{self.last_name} - {self.first_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.category_name}'


class Store(models.Model):
    store_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    store_image = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=32)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.store_name}, {self.address}'

    def get_average_rating(self):
        rating = self.store_reviews.all()
        if rating.exists():
            return sum([i.rating for i in rating]) / rating.count()
        return 0

    def get_count_people(self):
        rating = self.store_reviews.all()
        if rating.exists():
            return rating.count()
        return 0


class Contact(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='contact_store')
    title = models.CharField(max_length=32)
    contact_number = PhoneNumberField()
    social_network = models.CharField(max_length=62)


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    product_image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='product_store')

    def __str__(self):
        return f'{self.product_name}, {self.price}'


class Combo(models.Model):
    combo_name = models.CharField(max_length=32)
    description = models.TextField()
    combo_image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
    store = store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='combo_store')


def __str__(self):
    return f'{self.combo_name}, {self.combo_image}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f'{self.user}'


class CarItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    combo = models.CharField(max_length=32)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product}, {self.quantity}'


class Order(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Ожидает обработки', 'Ожидает обработки'),
        ('В процессе доставки', 'В процессе доставки'),
        ('Доставлен', 'Доставлен'),
        ('Отменен', 'Отменен')
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='Ожидает обработки')
    delivery_address = models.CharField(max_length=64)
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_orders')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.status}, {self.courier}'


class Courier(models.Model):
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier')
    current_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    TYPE_STATUS_CHOICES = (
        ('занят', 'занят'),
        ('доступен', 'доступен')
    )
    courier_status = models.CharField(max_length=16, choices=TYPE_STATUS_CHOICES)

    def __str__(self):
        return f'{self.courier} - {self.courier_status}'


class StoreReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_view')
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.store}'


class CourierRating(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_rating')
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.courier}'