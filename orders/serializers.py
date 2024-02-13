from rest_framework import serializers

from goods.serializers import FullProductSerializer
from orders.models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['product_id', 'quantity']
        extra_kwargs = {'product': {'write_only': True}}


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'phone_number', 'address', 'landmark', 'comment', 'products']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            product = product_data.pop('product')
            quantity = product_data.pop('quantity')
            OrderProduct.objects.create(order=order, product=product, quantity=quantity)
        return order


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



