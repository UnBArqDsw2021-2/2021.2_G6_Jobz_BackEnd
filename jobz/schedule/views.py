from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ScheduleSerializers
from .models import Schedule


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by("dayOfWeek")
    serializer_class = ScheduleSerializers
    permission_classes = [permissions.IsAuthenticated]
