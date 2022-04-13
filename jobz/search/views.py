from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OccupationSerializer
from .models import Occupation


class OccupationViewSet(viewsets.ModelViewSet):
    queryset = Occupation.objects.all().order_by("occupation")
    serializer_class = OccupationSerializer
    permission_classes = [permissions.IsAuthenticated]
