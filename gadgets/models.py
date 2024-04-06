# gadgets/models.py
from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    bio = models.TextField(blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True)

class Page(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Password(models.Model):
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.password

class Cart(models.Model):
    # One-to-One relationship with User for storing user's cart
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', default=None)

    def __str__(self):
        return self.name


class Order(models.Model):
    # Represents an order with user details, address, and associated products
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, default='New')
    address = models.CharField(max_length=255)
    products = models.TextField(blank=True)

class OrderItem(models.Model):
    # Represents an item in an order with quantity and total price
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=1000, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        # Calculate and set total_price before saving
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

class CartItem(models.Model):
    # Represents an item in a cart with quantity and total price
    id = models.BigAutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate and set total_price before saving
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
