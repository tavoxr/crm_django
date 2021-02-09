from django.forms import ModelForm
from django import forms
from .models import *



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields= '__all__'

    # customer = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  