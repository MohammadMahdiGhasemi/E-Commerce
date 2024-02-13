from django.shortcuts import render
from rest_framework import status 
from rest_framework .views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
class ProductView(APIView):
    model=Product
    serializer= ProductSerializer
    def get(self , request):
        category = request.GET.get('category' ,None)
        if category:
            products= self.model.objects.filter(category=category)
        else:
            products= self.model.objects.all()
        srz_data=self.serializer(instance=products , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)