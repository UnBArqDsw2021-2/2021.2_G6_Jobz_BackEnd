from .models import Schedule
from rest_framework import serializers

class ScheduleSerializers(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = '__all__'


	def validate(self, data):
		if data['entryTime'] < data['endOfWork']:
			raise serializers.ValidationError('123123123')
		return data
