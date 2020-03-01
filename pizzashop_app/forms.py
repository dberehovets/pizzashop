from django import forms
from django.contrib.auth.models import User
from pizzashop_app.models import PizzaShop


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class PizzaShopForm(forms.ModelForm):
    class Meta:
        model = PizzaShop
        fields = ('name', 'phone', 'address', 'logo')