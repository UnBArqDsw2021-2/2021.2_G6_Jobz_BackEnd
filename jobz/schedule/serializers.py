from .models import Schedule
from rest_framework import serializers

class ScheduleSerializers(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = ['dayOfWeek', 'entryTime', 'endOfWork', 'provider']
