from django.contrib import admin

from .models import Product, Client


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preço', 'estoque')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client)
