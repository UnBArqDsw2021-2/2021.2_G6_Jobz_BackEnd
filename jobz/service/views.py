from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ServiceSerializers
from .models import Services

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all().order_by('datePurchase')
    serializer_class = ServiceSerializers
    permission_classes = [permissions.IsAuthenticated]