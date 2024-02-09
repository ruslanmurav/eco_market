from django.contrib import admin
from django.urls import path, include
from goods.urls import goods_urlpatterns
from orders.urls import order_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goods/', include(goods_urlpatterns)),
    path('orders/', include(order_urlpatterns)),
]
