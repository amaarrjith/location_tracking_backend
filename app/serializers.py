from rest_framework import serializers
from app.models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = '__all__'