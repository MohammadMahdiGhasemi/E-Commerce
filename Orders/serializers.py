from rest_framework import serializers
from.models import Order , Discount_Code , OrderProduct , Transaction

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'person', 'date_time' , 'status' , 'transaction'] 



class DiscountCodeSerilizer(serializers.Serializer):
    class Meta:
        model=Discount_Code
        fields=['type','value','start_date', 'end_date' , 'code']




class OrderProductSerializer(serializers.Serializer):
    class Meta:
        model = OrderProduct
        fields = ['order' , 'product', 'quantity']



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [ 'amount' , 'date' ,'status' ]


