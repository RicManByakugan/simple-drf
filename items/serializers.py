from rest_framework import serializers
from .models import Items

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class CreateItemDTO(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name', 'price']

