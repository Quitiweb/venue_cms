from django.contrib import admin

from apps.home import models

admin.site.register([
    models.Campaign, models.Venue, models.Washroom,
    models.Media, models.WashroomGroups
])


class FaucetAdmin(admin.ModelAdmin):
    list_display = ['name', 'mac', 'ip_address', 'status']


admin.site.register(models.Faucet, FaucetAdmin)
