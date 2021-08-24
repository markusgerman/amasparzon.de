from django.contrib.auth import get_user_model
User = get_user_model()

#rest-framework
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email',)