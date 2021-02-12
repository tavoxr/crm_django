from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

