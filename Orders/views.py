from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Order , Discount_Code ,OrderProduct , Transaction
from .serializers import Ordrserializer , DiscountCodeSerilizer , OrderProductSerializer , TransactionSerializer
from rest_framework import status

class OrderView(APIView):
    model=Order
    serializer= Ordrserializer
    def get(self , request):
        orders= self.model.objects.all()
        srz_data=self.serializer(instance=orders , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    

class DiscountCodeView(APIView):
    model=Discount_Code
    serializer= DiscountCodeSerilizer
    def get(self , request):
        discount_codes= self.model.objects.all()
        srz_data=self.serializer(instance=discount_codes , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    

class OrderProductView(APIView):
    model=OrderProduct
    serializer= OrderProductSerializer
    def get(self , request):
        order_products= self.model.objects.all()
        srz_data=self.serializer(instance=order_products , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    

    
class TransactionView(APIView):
    model=Transaction
    serializer= TransactionSerializer
    def get(self , request):
        transanctions= self.model.objects.all()
        srz_data=self.serializer(instance=transanctions , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    