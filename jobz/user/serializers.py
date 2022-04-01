from .models import User, Provider
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
	password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
	class Meta:
		model = User
		fields = ['cpf' , 'name' , 'phone', 'email', 'password']

	def save(self):
		user = User(
			cpf = self.validated_data['cpf'],
            name = self.validated_data['name'],
            phone = self.validated_data['phone'],
            email = self.validated_data['email'],
        )
		password = self.validated_data['password']
		user.set_password(password)
		user.save()
		return user

class ProviderSerializers(serializers.ModelSerializer):
	password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Provider
		fields = ['cpf' , 'name' , 'phone', 'email', 'password']

	def save(self):
		provider = Provider(
			cpf = self.validated_data['cpf'],
			name = self.validated_data['name'],
			phone = self.validated_data['phone'],
			email = self.validated_data['email'],
    	)
		password = self.validated_data['password']
		provider.set_password(password)
		provider.save()
		return provider
