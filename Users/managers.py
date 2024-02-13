from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import BaseUserManager
from django.db.models import QuerySet

class PersonManager(BaseUserManager):
    # def create_user(self, email, password=None, **extra_fields):
    #     if not email:
    #         raise ValueError("Users must have an email address")
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    def create_user(self, phone_number, email, first_name, last_name, password):
        if not phone_number:
            raise ValueError("User must have a phone number")
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        # self.model is the model User!
        user = self.model(
        phone_number=phone_number,
        email=self.normalize_email(email),
        first_name=first_name,
        last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    # def create_superuser(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_admin', True)
        # # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_staff', True)
        # if extra_fields.get('is_admin') is not True:
        #     raise ValueError('Superuser must have is_admin=True.')
        # # if extra_fields.get('is_superuser') is not True:
        # #     raise ValueError('Superuser must have is_superuser=True.')
        # return self.create_user(email, password, **extra_fields)


    def create_superuser(self, phone_number, email, first_name, last_name, password):
            user = self.create_user(
            phone_number=phone_number,
            email=email,
            first_name=first_name,
            last_name = last_name,
            password=password,
            )
            user.is_staff = True
            user.save(using=self._db)
            return user