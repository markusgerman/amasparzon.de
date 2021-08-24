from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

#rest-framework
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins
from django.core.exceptions import PermissionDenied

class GenericUserList(generics.GenericAPIView, mixins.ListModelMixin,
                mixins.CreateModelMixin, mixins.UpdateModelMixin, 
                mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    lookup_field = 'id'
    
    def get(self, request, id = None):
        if id:
            if request.user.is_superuser:
                return self.retrieve(request)
            if request.user.id == id:
                return self.retrieve(request)
            else:
                raise PermissionDenied()
        else:
            return self.list(request)

    def post(self, request, id= None):
        return self.create(request)

    def delete(self, request, id):
        if request.user.is_superuser or request.user.id == id:   
            return self.destroy(request, id)
    
