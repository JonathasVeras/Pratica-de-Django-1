from django.contrib import admin

from .models import Product, Client


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'inventory')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
