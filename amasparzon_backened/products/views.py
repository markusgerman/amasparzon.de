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
        if Users.objects.filter(email = request.data['user']).exists():
            user = Users.objects.get(email = request.data['user'])
        else:
            Users.objects.create(email = request.data['user'])
            user = Users.objects.get(email = request.data['user'])

        request.data['user'] = user.id 

        product = Product.objects.get(asin = request.data['asin'])

        #check if user is already in product
        if user in product.user.all():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'User already in product'})

        #add user to the product
        product.user.add(user)

        #send email to user
        product.send_confirmation_mail(user)

        return Response(status=status.HTTP_201_CREATED)
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

        if results['name'] == None:
            return Response(status=status.HTTP_404_NOT_FOUND) 
                
        asin = re.search(r"/dp/[a-zA-Z0-9]+", request.get_full_path(), flags=re.IGNORECASE)
        if asin:
            asin = asin.group(0)[4:14]

        product = Product(
            name = results['name'],
            asin = asin,
            image = re.findall('"([^"]*)"', results['image'])[0],
        )

        serializer = AmazonProductSerializer(
            product,    
            context = {
                    'price' : results['price'],
                }
            )

        #check if product already exists and create if not
        if Product.objects.filter(asin = asin).exists() == False:
            product.save()
        
            #create first price for the product
            Price.objects.create(
                product = product,
                price = float(results['price'].replace('€','').replace(',','.')),
            ).save()

        return Response(serializer.data)
