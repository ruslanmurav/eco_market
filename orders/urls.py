from django.contrib import admin
from django.urls import path

from orders.views import temp

order_urlpatterns = [
    path('create/', temp, name='order-post'),
    # path('', temp, name='order-list'),
    # path('<int:id>', temp, name='order-get'),
]
