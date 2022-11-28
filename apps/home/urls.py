from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

    path('', views.index, name='home'),

    # Custom urls
    path('delete/<str:model>/<int:pk>', views.delete, name='delete_model'),
    path('campaigns', views.campaigns, name='campaigns'),
    path('venues', views.venues, name='venues'),
    path('faucets', views.faucets, name='faucets'),
    path('media', views.media, name='media'),
    path('reporting', views.reporting, name='reporting'),
    path('profile', views.profile, name='profile'),
]
