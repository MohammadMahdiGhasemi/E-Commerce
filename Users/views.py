from django.shortcuts import render
from rest_framework import status 
from rest_framework .views import APIView
from .models import Address ,Person
from .serializers import AddressSerializer ,PersonSerializer
from rest_framework.response import Response

class UserView(APIView):
    model=Person
    serializer=PersonSerializer 
    def get(self , request):
        persons= self.model.objects.all()
        srz_data=self.serializer(instance=persons , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        user= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=user , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , pk):
        user = self . model.objects.get(pk=pk)
        user.is_active=False
        user.save()
        return Response({'message':'User deleted'})    
class AddressView(APIView):
    model=Address
    serializer= AddressSerializer
    def get(self , request):
        addresses= self.model.objects.all()
        srz_data=self.serializer(instance=addresses , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        address= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=address , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        address = self.model.objects.get(pk=pk)
        address.is_active = False 
        address.save()
        return Response({'message': 'Address  deleted'})