from django.db.models import fields
from rest_framework import serializers

from drf_writable_nested import WritableNestedModelSerializer

from .models import Price, Product

class PriceSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Price
        exclude = ('product',)


class ProductSerializer(WritableNestedModelSerializer ,serializers.ModelSerializer):
    price_set = PriceSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'user', 'name', 'link', 'image', 'price_set')

class AmazonProductSerializer(serializers.ModelSerializer):

    price = serializers.SerializerMethodField('_get_price')

    class Meta:
        model = Product
        fields = (
            'name',
            'image',
            'price',
        )

    
    def _get_price(self, obj):
        price = self.context.get('price')
        return price
