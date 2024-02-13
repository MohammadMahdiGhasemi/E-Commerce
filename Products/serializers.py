from rest_framework import serializers
from .models import Category , Media , Discount,Product , Comment



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ['name' , 'parent']


class MediaSeerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields= ['image' , 'description']


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:

        model= Discount
        fields = ['type' , 'value', 'start_date','end_date', 'code']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields=['name' , 'brand','price','stock' , 'date_time' , 'discount', 'category' ,'media']



class CommentSerializr(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = '__all__'







