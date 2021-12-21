from django.http.response import Http404, HttpResponse

from amasparzon_backened.settings import FRONTEND_URL
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

#rest-framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import redirect


class UserList(APIView):

    def get(self, request, format=None):
        if request.user.is_admin:
            Users = User.objects.all()
            serializer = UserSerializer(Users, many=True)
            return Response(serializer.data)
            

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProfiView(APIView):
    """
    Delete the profile of the user if the delete hash is correct
    """
    def get(self, request, user_id, user_hash, format=None):

        #check if user has the right hash and delete the profile
        try:
            user = User.objects.get(id=user_id)
        except:
            return redirect(FRONTEND_URL)
            
        if user.user_hash == user_hash:
            user.delete()
            return redirect(FRONTEND_URL + '/profildelete')
        else:
            return redirect(FRONTEND_URL)