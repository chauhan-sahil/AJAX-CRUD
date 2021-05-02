from django.db import models
from django import forms

# Create your models here.

class CustomerForm(forms.Form):
    first_name=forms.CharField(max_length=25)
    last_name=forms.CharField(max_length=25)
    contact_no=forms.CharField(max_length=15)
    pincode=forms.IntegerField()

class ProductForm(forms.Form):
   name=forms.CharField(max_length=50) 
   unit_price=forms.DecimalField(max_digits=6,decimal_places=2)