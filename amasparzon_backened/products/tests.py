from products.models import Price, Product
from django.test import TestCase

class ProductTestCase(TestCase):
    
    def check_foreign_key_relation(self):
        product = Product.objects.create(name="Testprodukt", link = "/testprodukt/")
        Price.objects.create(price = 50.0, product = product)
      
