from .models import Person
from django.contrib.auth.backends import BaseBackend
class EmailBackend(BaseBackend):
    model = Person
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = self.model.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except self.model.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return self.model.objects.get(pk=user_id)
        except self.model.DoesNotExist:
            return None
        

from django.contrib.auth.backends import BaseBackend
from .models import Person

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Person.objects.get(email=email)

            if user.check_password(password):
                return user
        except Person.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Person.objects.get(pk=user_id)
        except Person.DoesNotExist:
            return None