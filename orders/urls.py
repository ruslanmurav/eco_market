from django.contrib import admin
from django.urls import path

from orders.views import temp, OrderCreateAPIView, OrderListAPIView, OrderDetailAPIView

order_urlpatterns = [
    path('create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('', OrderListAPIView.as_view(), name='order-list'),
    path('<int:id>/', OrderDetailAPIView.as_view(), name='order-detail'),
]
