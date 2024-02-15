from django.urls import path , include
from . import views
urlpatterns = [
    path('products/' , views.ProductView.as_view()),
    path('category/' , views.CategoryView.as_view()),
    path('media/' , views.MediaView.as_view()),
    path('discount/' , views.DiscountView.as_view()),
    path('comment/' , views.CommentView.as_view()),
    path('api/products/search/', views.ProductSearchAPIView.as_view()),
    
] 
