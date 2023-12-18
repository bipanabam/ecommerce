from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField 
# Create your models here.

class ProductGallery(models.Model):
    image = models.ImageField()

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to ='products/')
    description = RichTextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(null=True)
    view_count = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

    def increase_view_count(self):
        if self.view_count is None:
            self.view_count = 1
        else:
            self.view_count += 1
        self.save()
        
    def get_absolute_url(self):
        return reverse("shop:all")

    class Meta:
        ordering = ['-created_at']


class ProductGallery(models.Model):
    images = models.ImageField(upload_to ='products/')
