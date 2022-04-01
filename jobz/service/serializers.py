from .models import Services
from rest_framework import serializers

class ServiceSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Services
		fields = ['dateService', 'serviceDescription', 'user', 'provider', 'occupation']
