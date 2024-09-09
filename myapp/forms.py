from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from myapp.models import User, Product, Order, Return


class Register(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'number_of_product',)


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = (
            'quantity',
        )


class ReturnCreateForm(ModelForm):
    class Meta:
        model = Return
        fields = ()
