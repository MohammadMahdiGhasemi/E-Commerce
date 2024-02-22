from rest_framework import serializers
from .models import Address , Person , OTP
from django.contrib.auth import authenticate



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

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError('Invalid email or password')
        else:
            raise serializers.ValidationError('Must include "email" and "password"')
        
        return data