from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Account, UserAdmin as admin_user, MacUser


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
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avno_user', )}),
    )
    list_display = ['username', 'email', 'avno_user', ]


@admin.register(MacUser)
class MacUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mac_user', )}),
    )
    list_display = ['username', 'email', 'mac_user', ]
