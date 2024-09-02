from django.contrib.auth.views import LogoutView
from django.urls import path

from myapp.views import (Login, UserRegister, ProductListView, ProductCreateView,ProductDeleteView, ReturnDeleteView,
                         ProductUpdate, ProductDetailView, OrderListView,OrderCreateView, ReturnCreateView, ConfirmReturn,
                         ReturnListView, error_money, error_quantity) #confirm_return


urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', UserRegister.as_view(), name='register'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('save_order', OrderCreateView.as_view(), name='save_order'),
    path('order/', OrderListView.as_view(), name='order'),
    path('return/create/', ReturnCreateView.as_view(), name='return-create'),
    path('return/', ReturnListView.as_view(), name='return'),
    path('confirm-return/<int:pk>/', ConfirmReturn.as_view(), name='confirm-return'),
    path('return-delete/<int:pk>/', ReturnDeleteView.as_view(), name='return-delete'),
    path('error-money/', error_money, name='error-money'),
    path('error-quantity/', error_quantity, name='error-quantity'),
]