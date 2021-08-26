from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'), #Shows all products of a user
    path('products/<int:product_id>/', views.ProductDetail.as_view(), name='product-detail'), #Shows a certain product of a user
    #path('products/<int:product_id>/prices/', views.PriceList.as_view(), name='price-list'), #Shows the prices of a certain product of a user
]