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
    link = serializers.SerializerMethodField('_get_asin_aslink')

    class Meta:
        model = Product
        fields = ('asin', 'link', 'user', 'name', 'image', 'price_set')

    def _get_asin_aslink(self, obj):
        return obj.get_product_url()

class AmazonProductSerializer(serializers.ModelSerializer):

    price = serializers.SerializerMethodField('_get_price')
    link = serializers.SerializerMethodField('_get_asin_aslink')

    class Meta:
        model = Product
        fields = (
            'asin',
            'link',
            'name',
            'image',
            'price',
        )

    def _get_price(self, obj):
        price = self.context.get('price')
        return price

    def _get_asin_aslink(self, obj):
        return obj.get_product_url()
