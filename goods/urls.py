from django.contrib import admin
from django.urls import path

from goods.views import ListCategoryAPIView, ProductListAPIView

urlpatterns = [
    path('categories/', ListCategoryAPIView.as_view(), name='categories-list'),
    path('products/', ProductListAPIView.as_view(), name='products-list'),
    # path('products/<int:id>', template, name='product'),
]
