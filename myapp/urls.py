from django.contrib.auth.views import LogoutView
from django.urls import path

from myapp.views import (Login, UserRegister, ProductListView, ProductCreateView, ProductDeleteView, ProductUpdate,
                         ProductDetailView, OrderListView, OrderDeleteView, save_order, save_return, confirm_return,
                         ReturnListView)


urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', UserRegister.as_view(), name='register'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('save_order', save_order, name='save_order'),
    path('order/', OrderListView.as_view(), name='order'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
    path('return/create/', save_return, name='return-create'),
    path('return/', ReturnListView.as_view(), name='return'),
    path('confirm-return/', confirm_return, name='confirm-return'),

]
