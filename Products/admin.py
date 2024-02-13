from django.contrib import admin
from . models import Category , Media , Discount , Product , Comment

admin.site.register(Category)
admin.site.register(Media)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(Comment)