from rest_framework import viewsets
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
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])

        providers = Provider.objects.filter(name__contains=params['pk'])
        serializer = ProviderSerializers(providers, many=True)

        return Response(serializer.data)