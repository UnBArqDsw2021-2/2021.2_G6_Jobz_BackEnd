from .models import Services
from rest_framework import serializers

class ServiceSerializers(serializers.ModelSerializer):
	class Meta:
		model = Services
		fields = ['dateService', 'serviceDescription', 'user', 'provider', 'occupation']
