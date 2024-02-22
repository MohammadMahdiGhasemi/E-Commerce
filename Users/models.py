from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class PersonManager(models.Manager):
    pass

class Person(AbstractBaseUser, PermissionsMixin):
    CHOICES = (
        ("product manager", "Product Manager"),
        ("supervisor", "Supervisor"),
        ("operator", "Operator"),
        ("customer", "Customer"),
    )
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
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
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']
    
    def __str__(self):
        return self.username if self.username else self.email

class Address(models.Model):
    person = models.ForeignKey(Person , on_delete=models.CASCADE)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.person.first_name} - {self.person.last_name} - {self.country}"

class OTP(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.email} - {self.otp_code}"
