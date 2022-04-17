from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProviderPresentationSerializers
from .models import ProviderPresentation

class ProviderPresentationViewSet(viewsets.ModelViewSet):
    queryset = ProviderPresentation.objects.all().order_by('provider')
    serializer_class = ProviderPresentationSerializers
    permission_classes = [permissions.AllowAny]