from django.shortcuts import render
from rest_framework import status 
from rest_framework .views import APIView
from .models import Address
from .serializers import AddressSerializer
from rest_framework.response import Response
class AddressView(APIView):
    model=Address
    serializer= AddressSerializer
    def get(self , request):
        addresses= self.model.objects.all()
        srz_data=self.serializer(instance=addresses , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)