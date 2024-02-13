from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Person , Address
from .forms import UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin):
    list_display = ('email','role', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'is_admin')
    list_filter = ('is_active', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number','role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin','is_superuser' , 'groups' , 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_admin'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal=( 'groups' , 'user_permissions')

admin.site.register(Person, UserAdmin)

admin.site.register(Address)