from django.contrib import admin

from apps.home import models

admin.site.register([
    models.Venue,
    models.WashroomGroups
])


class MediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'campaign', 'type']


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'venues', 'start_date', 'end_date']


class FaucetAdmin(admin.ModelAdmin):
    list_display = ['name', 'mac', 'ip_address', 'status']


class WashroomAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "washroom_group", "venue"]


admin.site.register(models.Media, MediaAdmin)
admin.site.register(models.Campaign, CampaignAdmin)
admin.site.register(models.Faucet, FaucetAdmin)
admin.site.register(models.Washroom, WashroomAdmin)

