from rest_framework import serializers
from .models import Address
class AddressSerializer(serializers.Serializer):
    model =Address
    fields = '__all__'