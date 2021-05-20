from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from sales.serializers import ProductSerializer, ProductDetailSerializer, ProductPriceSerializer, ProductPricePostSerializer
from sales.models import Product, ProductPrice

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(APIView):
    """
    List all products or create a new one
    """

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    """
    Get, update, or delete a product
    """

    def get(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductDetailSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.update(product, request.data)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProductPriceView(APIView):
    """
    List all prices for one product or create a new one
    """
    
    def get(self, request, productId, format=None):
        productPrices = ProductPrice.objects.filter(product = productId)
        serializer = ProductPriceSerializer(productPrices, many=True)
        return Response(serializer.data)
        #TODO 404

    def post(self, request, productId, format=None):
        try:
            productPriceSerializer = ProductPricePostSerializer(data=request.data)

            if productPriceSerializer.is_valid():
                product = Product.objects.get(pk=productId)
                productPrice = ProductPrice.objects.create(product=product, price=productPriceSerializer.validated_data['price'], date=timezone.now())
                productPrice.save()
                serializer = ProductPriceSerializer(productPrice)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(productPriceSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)