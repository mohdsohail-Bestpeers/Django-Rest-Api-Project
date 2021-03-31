from rest_framework import  serializers
from .models import React


class React_Serializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['Name','Detail']