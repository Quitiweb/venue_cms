from django.contrib import admin

from home import models

admin.site.register([
    models.Campaign, models.Venue, models.Washroom,
    models.Faucet, models.Media,
])
