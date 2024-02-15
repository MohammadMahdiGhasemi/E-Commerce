from django.urls import path , include
from . import views
urlpatterns = [
 path('orders/' , views.OrderView.as_view()),
 path('discount/' , views.DiscountCodeView.as_view()),
 path('order_product/' , views.OrderProductView.as_view()),
 path('transaction/' , views.TransactionView.as_view()),
] 
