from django.contrib import admin
from django.urls import path

from goods.views import ListCategoryAPIView

urlpatterns = [
    path('categories/', ListCategoryAPIView.as_view(), name='categories-list'),
    path('products/', template, name='products-list'),
    path('products/<int:id>', template, name='product'),
]
