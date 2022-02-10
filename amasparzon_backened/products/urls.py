from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    #path('products/<int:product_id>/', views.ProductDetail.as_view(), name='product-detail'),
    path('products/<path:product_resource>', views.AmazonProduct.as_view(), name='amazon-detail'),
]

