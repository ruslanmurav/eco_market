from django.contrib import admin
from django.urls import path

from goods.views import ListCategoryAPIView, ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path('categories/', ListCategoryAPIView.as_view(), name='categories-list'),
    path('products/<int:category_id>/', ProductListAPIView.as_view(), name='products-list'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product'),
]
