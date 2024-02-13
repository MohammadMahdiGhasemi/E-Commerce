from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import PersonManager


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Person(AbstractBaseUser, PermissionsMixin):
    CHOICES = (
("product manager", "Product Manager"),
("supervisor", "Supervisor"),
("operator", "Operator"),
("customer", "Customer"),
)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=100, blank=True , choices=CHOICES)
    date_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = PersonManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','first_name' , 'last_name']
    
    def __str__(self):
        return self.username if self.username else self.email
    
    # def has_perm(self, perm, obj=None):
    #     return True
    # def has_module_perms(self, app_label):
    #     return True


class Address(models.Model):
    person=models.ForeignKey(Person ,on_delete=models.CASCADE)
    country = models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    street =models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.person.first_name} - {self.person.last_name} - {self.country}"