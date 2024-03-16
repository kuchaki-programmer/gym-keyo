from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Otp


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('phone', 'email', 'full_name')
    list_filter = ('is_staff',)
    ordering = ('-created_at',)
    list_display = ('phone', 'username', 'email', 'full_name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('phone', 'email', 'username')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('full_name', )})
    )
    add_fieldsets = (
        (None, {'fields': ('phone', 'username', 'email', 'full_name', 'password1', 'password2', 'age', 'is_staff', 'is_active')}),
    )


admin.site.register(CustomUser, UserAdminConfig)
admin.site.register(Otp)

