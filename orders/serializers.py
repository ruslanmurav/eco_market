from rest_framework import serializers

from orders.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = []


class OrderShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total_cost']
