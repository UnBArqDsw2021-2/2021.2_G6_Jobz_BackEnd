from .models import Occupation
from rest_framework import serializers

class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ['occupation']