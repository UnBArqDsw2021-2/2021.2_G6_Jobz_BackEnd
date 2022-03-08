from .models import User, Provider 
from rest_framework import serializers

class UserSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['cpf' , 'name' , 'phone', 'email']

class ProviderSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Provider
		fields = ['cpf' , 'name' , 'phone', 'email']
