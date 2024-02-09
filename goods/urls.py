from django.contrib import admin
from django.urls import path

from goods.views import template

urlpatterns = [
    path('categories/', template, name='categories-list'),
    path('products/', template, name='products-list'),
    path('products/<int:id>', template, name='product'),
]
