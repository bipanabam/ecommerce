from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ("shipping_address","phone_number","payment_method")