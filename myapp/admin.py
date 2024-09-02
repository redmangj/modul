from django.contrib import admin
from myapp.models import User, Product, Order, Return


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'number_of_product', 'created_at')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'wallet')


class ReturnAdmin(admin.ModelAdmin):
    list_display = ('order', 'created_at')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', )

class ReturnAdmin(admin.ModelAdmin):
    list_display = ('id', )


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Return, ReturnAdmin)
