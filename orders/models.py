from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'), 
        ('confirmed', 'Confirmed'), 
        ('failed', 'Failed')
    ], default='pending')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()