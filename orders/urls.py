from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from orders.views import OrderCreateAPIView, OrderListAPIView, OrderDetailAPIView


order_urlpatterns = [
    path('create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('', OrderListAPIView.as_view(), name='order-list'),
    path('<int:id>/', OrderDetailAPIView.as_view(), name='order-detail'),
]
