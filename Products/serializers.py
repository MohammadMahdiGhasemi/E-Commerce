from rest_framework import serializers
from .models import Category , Media , Discount,Product , Comment



class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields= ['name' , 'parent']


class MediaSeerializer(serializers.Serializer):
    model = Media
    fields= ['image' , 'description']


class DiscountSerializer(serializers.Serializer):
    model= Discount
    fields = ['type' , 'value', 'start_date','end_date', 'code']



class ProductSerializer(serializers.Serializer):
    model= Product
    fields='__all__'


class CommentSerializr(serializers.Serializer):
    model= Comment
    fields = '__all__'







