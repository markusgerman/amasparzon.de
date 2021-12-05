from django.http.response import Http404, HttpResponse
from django.shortcuts import render
import re

#custom user model
from django.contrib.auth import get_user_model
Users = get_user_model()

#rest-framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Price, Product, User
from .serializers import AmazonProductSerializer, ProductSerializer, PriceSerializer
from products import serializers

from modules.webscraper import amazon

class ProductList(APIView):
    """
    Productlist of the requested user
    """

    def get(self, request, format=None):
        products = Product.objects.filter(user = request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        
        #check if user exists and create if not
        if Users.objects.filter(email = request.data['email']).exists():
            pass
        else:
            Users.objects.create(email = request.data['email'])
        

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    Productdetail of the request product
    """

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


class AmazonProduct(APIView):
    
    def get(self, request, product_resource, format=None):

        results = amazon.scrape(product_resource)
    
        product = Product(
            name= results['name'],
            link = "",
            image = re.findall('"([^"]*)"', results['image'])[0],
        )

        serializer = AmazonProductSerializer(
            product,
            context = {
                    'price' : results['price'],
                }
            )

        return Response(serializer.data)
