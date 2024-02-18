from django.urls import path , include
from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('users/' , views.UserView.as_view(),name='user'),
    path('users/<int:pk>' , views.UserView.as_view(),name='user-pk'),
    path('address/' , views.AddressView.as_view(),name='address'),
    path('address/<int:pk>' , views.AddressView.as_view(),name='address-pk'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 