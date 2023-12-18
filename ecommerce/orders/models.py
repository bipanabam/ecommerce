from django.db import models

from shop.models import Product
from authentication.models import CustomUser

# Create your models here.
class Cart(models.Model):
    cart_count = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_quantity = models.IntegerField(default=1)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, related_name='user_cart')

    def __str__(self):
        return str(self.cart_count)

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

# class PaymentMethod(models.Model):
#     name = models.CharField(max_length=256)

#     def __str__(self):
#         return self.name
    

class Order(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, null=True)
    total = models.PositiveIntegerField()
    status = models.CharField(max_length=256, default='pending')
    shipping_address = models.CharField(max_length=256, null=True)
    phone_number = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=256,default="Cash On Delivery")
    user = models.ForeignKey(CustomUser,related_name='orders',on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payment_method

    def change_status(self):
        self.status = 'Delivered'
        self.save()

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
    
    