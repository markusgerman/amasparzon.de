from django.db.models import fields
from rest_framework import serializers

from .models import Price, Product

class PriceSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Price
        exclude = ('product',)


class ProductSerializer(serializers.ModelSerializer):
    price_set = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'user', 'name', 'link', 'image', 'price_set')