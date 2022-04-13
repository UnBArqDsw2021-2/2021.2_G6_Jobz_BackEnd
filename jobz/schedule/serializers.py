from .models import Schedule
from rest_framework import serializers

class ScheduleSerializers(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = '__all__'


	def save(self):
		start = self.validated_data['entryTime']
		end = self.validated_data['endOfWork']
		if end < start:
			raise serializers.ValidationError('O Horário de saida não pode ser anterior ao horário de entrada.')
		else:
			schedule = Schedule (
				entryTime = start,
				endOfWork = end,
				dayOfWeek = self.validated_data['dayOfWeek'],
				provider = self.validated_data['provider'],
			)
			schedule.save()
			return schedule
