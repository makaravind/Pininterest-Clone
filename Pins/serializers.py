from rest_framework import serializers
from .models import Pin

class PinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pin
        fields = ['tagline', 'created_on', 'updated_on', 'likes', 'interest']
