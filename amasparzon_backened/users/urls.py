from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('users/<int:id>', views.GenericUserList.as_view(), name='user-list'),
]