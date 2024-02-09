from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('categories/', ..., name='categories-list'),
    path('products/', ..., name='products-list'),
    path('products/<int:id>', ..., name='product'),
]
