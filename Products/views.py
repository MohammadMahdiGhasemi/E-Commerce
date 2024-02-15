from django.shortcuts import render
from rest_framework import status 
from rest_framework .views import APIView
from .models import Product , Category ,Media ,Discount , Comment
from .serializers import ProductSerializer ,CategorySerializer , MediaSerializer , DiscountSerializer , CommentSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
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
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        product= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=product , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.model.objects.get(pk=pk)
        product.is_active = False 
        product.save()
        return Response({'message': 'product  deleted'})
    

class ProductSearchAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']
    

class CategoryView(APIView):
    model=Category
    serializer= CategorySerializer
    def get(self , request):
        categories= self.model.objects.all()
        srz_data=self.serializer(instance=categories , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        category= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=category , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category = self.model.objects.get(pk=pk)
        category.is_active = False 
        category.save()
        return Response({'message': 'category  deleted'})
    

class MediaView(APIView):
    model=Media
    serializer= MediaSerializer
    def get(self , request):
        medeis= self.model.objects.all()
        srz_data=self.serializer(instance=medeis , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        media= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=media , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        media = self.model.objects.get(pk=pk)
        media.is_active = False 
        media.save()
        return Response({'message': 'category  deleted'})
    


class DiscountView(APIView):
    model=Discount
    serializer= DiscountSerializer
    def get(self , request):
        discounts= self.model.objects.all()
        srz_data=self.serializer(instance=discounts , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        discount= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=discount , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        discount = self.model.objects.get(pk=pk)
        discount.is_active = False 
        discount.save()
        return Response({'message': 'discount  deleted'})
    

class CommentView(APIView):
    model=Comment
    serializer= CommentSerializer
    def get(self , request):
        comments= self.model.objects.all()
        srz_data=self.serializer(instance=comments , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        comment= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=comment , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        comment = self.model.objects.get(pk=pk)
        comment.is_active = False 
        comment.save()
        return Response({'message': 'comment  deleted'})