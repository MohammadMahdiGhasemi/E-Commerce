from rest_framework import serializers
from.models import Order , Discount_Code , OrderProduct , Transaction

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['discount' , 'date_time' , 'status']



class DiscountCodeSerilizer(serializers.Serializer):
    class Meta:
        model=Discount_Code
        fields=['type','value','start_date', 'end_date' , 'code']




class OrderProductSerializer(serializers.Serializer):
    class Meta:
        model = OrderProduct
        fields = ['order' , 'product', 'quantity']



class TransactionSerializer(serializers.Serializer):
    model = Transaction
    fields = ['order' , 'person' , 'amount' , 'date' ,'status' ]


