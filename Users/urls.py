from django.urls import path , include
from . import views
urlpatterns = [
    path('users/' , views.UserView.as_view()),
    path('address/' , views.AddressView.as_view())
] 