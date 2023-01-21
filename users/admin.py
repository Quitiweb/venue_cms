from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Account, UserAdmin as admin_user


@admin.register(Account)
class AccountAdmin(UserAdmin):
    """
        Account model admin
    """
    search_fields = ('username',)
    ordering = ('username', 'is_superuser', 'is_active',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'is_avno', )}),
    )
    list_display = ['username', 'email', 'is_staff', 'is_superuser', 'is_avno']


@admin.register(admin_user)
class AdminUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'avno_user', ]
