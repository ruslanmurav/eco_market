from django.contrib import admin
from django.urls import path, include
from goods.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goods/', include(urlpatterns)),
]
