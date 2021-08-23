from django.http.response import Http404
from django.shortcuts import render

#rest-framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from .serializers import UserSerializer
from user import serializers


class UserDetail(APIView):

    def get_object(self, id):
        try:
            return User.objects.get(id = id) #.get(slug=product_slug)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):

        serializer_context = {
            'request': request,
        }
        user = self.get_object(id = id)
        serializer = UserSerializer(user, context=serializer_context)
        return Response(serializer.data)

