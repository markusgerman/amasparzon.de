from django.http.response import Http404, HttpResponse
from django.shortcuts import render

#rest-framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Price, Product
from .serializers import ProductSerializer, PriceSerializer
from products import serializers



class ProductList(APIView):

    def get(self, request, format=None):
        products = Product.objects.filter(user = request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get_object(self, product_id):
        try:
            return Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            raise Http405

    def get(self, request, product_id, format=None):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, product_id, format=None):
        product = self.get_object(product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
