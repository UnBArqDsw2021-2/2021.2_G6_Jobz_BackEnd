from .models import ProviderPresentation
from rest_framework import serializers

class ProviderPresentationSerializers(serializers.ModelSerializer):
	class Meta:
		model = ProviderPresentation
		fields = '__all__'
