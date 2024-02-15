from rest_framework import serializers
from .models import Address , Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model =Person
        fields = '__all__'
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model =Address
        fields = '__all__'