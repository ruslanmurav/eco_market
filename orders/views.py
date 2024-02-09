from rest_framework.generics import CreateAPIView

from orders.models import Order
from orders.serializers import OrderCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
