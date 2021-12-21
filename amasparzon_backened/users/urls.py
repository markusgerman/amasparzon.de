from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/delete/<int:user_id>/<uuid:user_hash>', views.DeleteProfiView.as_view(), name='delete-profile'),
]