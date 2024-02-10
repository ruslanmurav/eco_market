from rest_framework import serializers

from goods.serializers import FullProductSerializer
from orders.models import Order, OrderProduct


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    products = FullProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'products']


class OrderShortSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()

    def get_total_cost(self, obj):
        total = sum(item.product.price * item.quantity for item in obj.orderproduct_set.all())
        return total

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total_cost']
