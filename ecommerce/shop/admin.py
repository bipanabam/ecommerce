from django.contrib import admin
from django import forms

from . import models

from ckeditor.widgets import CKEditorWidget


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ('name','image','description','price','quantity')

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

admin.site.register(models.Product, ProductAdmin)

admin.site.register(models.Category)
admin.site.register(models.ProductGallery)