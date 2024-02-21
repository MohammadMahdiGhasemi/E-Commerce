from rest_framework import serializers
from .models import Address , Person , OTP


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model =Person
        fields = '__all__'
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model =Address
        fields = '__all__'


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'