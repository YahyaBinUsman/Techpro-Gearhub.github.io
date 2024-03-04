# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Order

# SignUpForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# CheckoutForm
class CheckoutForm(forms.ModelForm):
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(label='ZIP Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ['address', 'city', 'state', 'zip_code', 'phone_number', 'country']

# ProductForm
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

# AddProductForm
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

# PasswordForm
class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)