from django.urls import path
from . import views



app_name = 'products'
urlpatterns = [
    path('users/<int:user_id>/products/', views.ProductList.as_view(), name='product-list'),
    path('users/<int:user_id>/products/<int:product_id>', views.ProductDetail.as_view(), name='product-detail'),
    path('users/<int:user_id>/products/<slug:product_id>/prices/', views.PriceList.as_view(), name='price-list'),
]