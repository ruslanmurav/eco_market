from django.contrib import admin

from goods.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'price', 'description']
