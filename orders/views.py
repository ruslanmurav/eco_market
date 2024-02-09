from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from orders.models import Order
from orders.serializers import OrderCreateSerializer, OrderShortSerializer, OrderDetailSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderShortSerializer


class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = 'id'
