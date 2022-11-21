from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    # Custom urls
    path('campaigns', views.campaigns, name='campaigns'),
    path('venues', views.venues, name='venues'),
    path('faucets', views.faucets, name='faucets'),
    path('media', views.media, name='media'),
    path('reporting', views.reporting, name='reporting'),
    path('profile', views.profile, name='profile'),
]
