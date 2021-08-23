from django.http.response import Http404, HttpResponse
from django.shortcuts import render

#rest-framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Price, Product
from .serializers import ProductSerializer, PriceSerializer


class ProductList(APIView):

    def get(self, request, user_id, format=None):
        products = Product.objects.filter(user_id = user_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductDetail(APIView):

    def get_object(self, user_id, product_id):
        try:
            return Product.objects.filter(id=product_id, user_id = user_id)
        except Product.DoesNotExist:
            raise Http404
    

    def get(self, request, user_id, product_id, format=None):
        product = self.get_object(user_id, product_id)
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data)



class PriceList(APIView):

    def get(self, request, user_id, product_id, format=None):
        products = Price.objects.filter(product_id = product_id)
        serializer = PriceSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    