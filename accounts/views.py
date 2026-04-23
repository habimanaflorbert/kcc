from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import UserSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.filter()
    serializer_class=UserSerializer

    def create(self, request, *args, **kwargs):
        serializer_class=self.get_serializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        
    
    