from rest_framework import serializers
from .models import Category , Media , Discount,Product , Comment



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ['name' , 'parent']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields= ['image' , 'description']


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:

        model= Discount
        fields = ['type' , 'value', 'start_date_time','end_date_time', 'code']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields=['name' , 'brand','price','stock' , 'date_time' , 'discount', 'category' ,'media']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = '__all__'







