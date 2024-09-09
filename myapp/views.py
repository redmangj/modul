from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from decimal import Decimal

from myapp.forms import Register, ProductCreateForm, OrderCreateForm, ReturnCreateForm
from myapp.models import Product, Order, User, Return


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'myapp/login.html'


class UserRegister(CreateView):
    form_class = Register
    template_name = 'myapp/register.html'
    success_url = '/login'


class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    paginate_by = 5
    extra_context = {'create_form': OrderCreateForm()}


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'myapp/product-create.html'
    form_class = ProductCreateForm
    success_url = '/'


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'description', 'price', 'number_of_product',)
    template_name = 'myapp/product-update.html'
    success_url = '/'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "myapp/product.html"
    model = Product
    extra_context = {'create_form': OrderCreateForm()}


class OrderCreateView(CreateView):
    form_class = OrderCreateForm
    http_method_names = ['post']
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.product = Product.objects.get(pk=self.request.POST['id'])
        obj.total = Decimal(obj.product.price) * Decimal(obj.quantity)
        number_of_product = int(obj.product.number_of_product)
        wallet = Decimal(obj.user.wallet)
        new_number_of_product = number_of_product - obj.quantity
        new_wallet = wallet - obj.total
        if number_of_product < obj.quantity:
            return redirect('error-quantity')
        if wallet < obj.total:
            return redirect('error-money')
        else:
            obj.save()
            User.objects.filter(pk=self.request.user.id).update(wallet=new_wallet)
            Product.objects.filter(pk=self.request.POST['id']).update(number_of_product=new_number_of_product)
            return super().form_valid(form=form)


def error_money(request):
    return render(request, 'myapp/error-money.html')


def error_quantity(request):
    return render(request, 'myapp/error-quantity.html')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'myapp/order.html'
    paginate_by = 100


class ReturnListView(LoginRequiredMixin, ListView):
    model = Return
    template_name = 'myapp/return.html'
    paginate_by = 100


class ReturnCreateView(CreateView):
    form_class = ReturnCreateForm
    http_method_names = ['post']
    success_url = '/order'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.order = Order.objects.get(pk=self.request.POST['id'])
        obj.save()
        return super().form_valid(form=form)


class ConfirmReturn(View):
    model = Return
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        return_id = Return.objects.get(pk=self.kwargs.get('pk'))
        order = Order.objects.get(pk=return_id.order.id)
        quantity = int(order.quantity)
        total = order.total
        wallet = order.user.wallet
        number_of_product = int(order.product.number_of_product)
        return_wallet = wallet + total
        return_number_of_product = number_of_product + quantity
        User.objects.filter(pk=order.user.id).update(wallet=return_wallet)
        Product.objects.filter(pk=order.product.id).update(number_of_product=return_number_of_product)
        order.delete()
        return redirect('/return')


class ReturnDeleteView(DeleteView):
    model = Return
    success_url = '/return'


class MyView(View):
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
