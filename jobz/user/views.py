from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializers, ProviderSerializers
from .models import User, Provider

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializers
    permission_classes = [permissions.IsAuthenticated]