from rest_framework import serializers
from .models import ImagesModel

class ImagesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = '__all__'