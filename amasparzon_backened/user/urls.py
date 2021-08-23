from django.urls import path
from . import views



app_name = 'user'
urlpatterns = [
    path('users/<int:id>/', views.UserDetail.as_view(), name='user-detail'),
]