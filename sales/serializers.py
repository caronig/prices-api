from sales.models import Product, ProductPrice
from rest_framework import serializers

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['product', 'price', 'date']

class ProductPricePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['price']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class ProductDetailSerializer(serializers.ModelSerializer):
    prices = ProductPriceSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'prices']