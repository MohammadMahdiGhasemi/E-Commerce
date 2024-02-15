from django.urls import path , include
from . import views
urlpatterns = [
    path('users/' , views.UserView.as_view(),name='user'),
    path('users/<int:pk>' , views.UserView.as_view(),name='user-pk'),
    path('address/' , views.AddressView.as_view(),name='address'),
    path('address/<int:pk>' , views.AddressView.as_view(),name='address-pk'),
] 