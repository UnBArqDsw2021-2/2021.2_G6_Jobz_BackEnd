from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UserSerializers, ProviderSerializers
from .models import User, Provider

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializers
    permission_classes = [permissions.AllowAny]

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializers
    filterset_fields = ['name']
    permission_classes = [permissions.AllowAny]

class ProviderList(generics.ListAPIView):
    serializer_class = ProviderSerializers

    def get_queryset(self):
        name = self.kwargs['name']
        occupation = self.kwargs['occupation']

        if name == '-':
            if occupation == 0:
                return Provider.objects.all()
            else:
                return Provider.objects.filter(occupation=occupation)
        else:
            if occupation == 0:
                return Provider.objects.filter(name__contains=name)
            else:
                return Provider.objects.filter(name__contains=name, occupation=occupation)
    