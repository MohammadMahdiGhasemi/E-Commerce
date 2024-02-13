from django.db import models
from Users.models import Person
from Products.models import Product



class Discount_Code(models.Model):
    type = models.CharField(max_length=250 , choices=[('perecentage', 'Perecentage'), ('decimal', 'Decimal')])
    value=models.DecimalField(max_digits=5, decimal_places=2)
    start_date_time=models.DateTimeField(auto_now_add=True)
    end_date_time=models.DateTimeField(auto_now_add=True)
    code=models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.code} - {self.start_date_time} - {self.end_date_time}"

class Order (models.Model):
    person = models.ForeignKey(Person , on_delete=models.CASCADE )
    discount_code = models.ForeignKey(Discount_Code , on_delete=models.CASCADE, blank=True  , null=True)
    date_time=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'{self.id} - {self.person} - {self.status}'




class OrderProduct(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self) -> str:
        return f"{self.order.person} -{self.product}"


class Transaction(models.Model):
    order=models.ForeignKey(Order , on_delete=models.CASCADE )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('success', 'Success'), ('failure', 'Failure') , ('none' , 'None')])

    def __str__(self) -> str:
        return f"{self.order.person} - {self.order}"