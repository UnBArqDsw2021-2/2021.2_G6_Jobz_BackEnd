from datetime import date
from .models import Services
from rest_framework import serializers

class ServiceSerializers(serializers.ModelSerializer):
	class Meta:
		model = Services
		fields = ['dateService', 'serviceDescription', 'user', 'provider', 'occupation']


	def save(self):
		scheduledDay = self.validated_data['dateService']
		if scheduledDay < date.today():
			raise serializers.ValidationError('A data do serviço deve ser posterior a data atual.')
		else:
			service = Services (
				dateService = scheduledDay,
				serviceDescription = self.validated_data['serviceDescription'],
				user = self.validated_data['user'],
				provider = self.validated_data['provider'],
				occupation = self.validated_data['occupation'],
			)
			service.save()
			return service
