from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Product,Order

class CreateProduct(ModelForm):
    
    
    class Meta:
        model=Product
        fields= '__all__'

class CreateOrder(ModelForm):

    class Meta:
        model=Order
        fields=['product','order_quantity']