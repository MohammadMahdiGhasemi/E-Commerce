from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Order , Discount_Code ,OrderProduct , Transaction
from .serializers import OrderSerializer , DiscountCodeSerilizer , OrderProductSerializer , TransactionSerializer
from rest_framework import status

class OrderView(APIView):
    model=Order
    serializer= OrderSerializer
    def get(self , request):
        orders= self.model.objects.all()
        srz_data=self.serializer(instance=orders , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        order= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=order , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        order = self.model.objects.get(pk=pk)
        order.is_active = False 
        order.save()
        return Response({'message': 'order deleted'})
    

class DiscountCodeView(APIView):
    model=Discount_Code
    serializer= DiscountCodeSerilizer
    def get(self , request):
        discount_codes= self.model.objects.all()
        srz_data=self.serializer(instance=discount_codes , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        discount_code= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=discount_code , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        discount_code = self.model.objects.get(pk=pk)
        discount_code.is_active = False 
        discount_code.save()
        return Response({'message': 'discount_code  deleted'})
    

class OrderProductView(APIView):
    model=OrderProduct
    serializer= OrderProductSerializer
    def get(self , request):
        order_products= self.model.objects.all()
        srz_data=self.serializer(instance=order_products , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        order_product= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=order_product , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        order_product = self.model.objects.get(pk=pk)
        order_product.is_active = False 
        order_product.save()
        return Response({'message': 'order_product  deleted'})

    
class TransactionView(APIView):
    model=Transaction
    serializer= TransactionSerializer
    def get(self , request):
        transanctions= self.model.objects.all()
        srz_data=self.serializer(instance=transanctions , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        transaction= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=transaction, data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        transaction= self.model.objects.get(pk=pk)
        transaction.is_active = False 
        transaction.save()
        return Response({'message': 'transaction  deleted'})