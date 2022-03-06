from .models import Services
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ServiceSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Services
		fields = ['datePurchase' , 'dateSevice' , 'serviceDesription']
