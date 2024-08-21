from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from myapp.forms import Register, ProductCreateForm
from myapp.models import Product, Order, User, Return


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'myapp/login.html'


class UserRegister(CreateView):
    form_class = Register
    template_name = 'myapp/register.html'
    success_url = '/'


class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    paginate_by = 5


class ProductCreateView(CreateView):
    template_name = 'myapp/product-create.html'
    form_class = ProductCreateForm
    success_url = '/'


class ProductUpdate(UpdateView):
    model = Product
    fields = ('name', 'description', 'price', 'number_of_product',)
    template_name = 'myapp/product-update.html'
    success_url = '/'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'


class ProductDetailView(DetailView):
    template_name = "myapp/product.html"
    model = Product


def save_order(request):
    user = request.user
    product = Product.objects.get(pk=request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    total = float(request.POST['price']) * float(request.POST['quantity'])
    number_of_product = int(request.POST['number_of_product'])
    new_number_of_product = number_of_product - quantity
    wallet = float(request.POST['wallet']) - total
    if number_of_product >= quantity and wallet >= total:
        Order(user=user, product=product, quantity=quantity, total=total).save()
        User.objects.filter(pk=request.POST['user']).update(wallet=wallet)
        Product.objects.filter(pk=request.POST['product_id']).update(number_of_product=new_number_of_product)
        return redirect('/')
    else:
        return HttpResponse(f'We dont have that numbers of product or you dont have enough money!')


class OrderListView(ListView):
    model = Order
    template_name = 'myapp/order.html'
    paginate_by = 100


class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/'


class ReturnListView(ListView):
    model = Return
    template_name = 'myapp/return.html'
    paginate_by = 100


def save_return(request):
    order = Order.objects.get(pk=request.POST['order'])
    Return(order=order).save()
    return redirect('/')


def confirm_return(request):
    order = Order.objects.get(pk=request.POST['order'])
    quantity = int(request.POST['quantity'])
    number_of_product = int(request.POST['number_of_product'])
    new_number_of_product = number_of_product + quantity
    total = float(request.POST['total'])
    wallet = float(request.POST['wallet']) + total
    User.objects.filter(pk=request.POST['user']).update(wallet=wallet)
    Product.objects.filter(pk=request.POST['product_id']).update(number_of_product=new_number_of_product)
    order.delete()
    return redirect('/')