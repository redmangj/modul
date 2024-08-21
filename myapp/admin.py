from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from myapp.models import User, Product, Order, Return


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'number_of_product', 'created_at')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'wallet')


class ReturnAdmin(admin.ModelAdmin):
    list_display = ('order', 'created_at')


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Return, ReturnAdmin)

