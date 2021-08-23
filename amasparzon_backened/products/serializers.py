from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers

from .models import Price, Product

class PriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Price
        exclude = ('product',)

class ProductSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        exclude = ('user',)