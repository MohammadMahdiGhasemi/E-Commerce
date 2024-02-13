from django.db import models

from Users.models import Person


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    
    def __str__(self) -> str:
        return self.name


class Media(models.Model):
    image= models.ImageField()
    description=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.description

class Discount(models.Model):
    type = models.CharField(max_length=250 , choices=[('perecentage', 'Perecentage'), ('decimal', 'Decimal')])
    value=models.DecimalField(max_digits=5, decimal_places=2)
    start_date_time=models.DateTimeField(auto_now_add=True)
    end_date_time=models.DateTimeField(auto_now_add=True)
    code=models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.code} - {self.start_date_time} - {self.end_date_time}"




class Product(models.Model):
    name=models.CharField(max_length=250)
    brand=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    stock = models.CharField(max_length=250, choices=[('avalible', 'Avalible'), ('finished', 'Finished')])
    date_time=models.DateTimeField(auto_now_add=True)
    discount=models.ForeignKey(Discount , on_delete=models.CASCADE , blank=True  , null=True)
    category= models.ForeignKey(Category , on_delete=models.CASCADE )
    media=models.ForeignKey(Media , on_delete=models.CASCADE, blank=True  , null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.category} - {self.brand}"



class Comment(models.Model):
    product= models.ForeignKey(Product , on_delete=models.CASCADE)
    person = models.ForeignKey(Person , on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    created_at= models.DateTimeField(auto_now_add=True)
    parent_comment= models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f'{self.person} - {self.product}'

