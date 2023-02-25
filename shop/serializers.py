from rest_framework import serializers

from .models import *
from account.publicserializers import PubUserSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'paid', 'amount', 'created_on', 'updated_on']

    def to_representation(self, instance):
        self.fields['user'] = PubUserSerializer(many=False)
        return super(OrderSerializer, self).to_representation(instance)


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['product', 'price', 'quantity', 'created_on', 'updated_on']

    def to_representation(self, instance):
        self.fields['product'] = ProductSerializer(many=False)
        return super(OrderSerializer, self).to_representation(instance)

