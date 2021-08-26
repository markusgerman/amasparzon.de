from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
]