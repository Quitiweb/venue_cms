from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

    path('', views.index, name='home'),
    path('add/<str:model>/new_record', views.create_new_record, name='add_new_record'),
    path('delete/<str:model>/<int:pk>', views.delete, name='delete_model'),
    path('update/<str:model>/<int:pk>', views.update, name='update_model'),
    path('campaigns', views.campaigns, name='campaigns'),
    path('venues', views.venues, name='venues'),
    path('washrooms', views.washrooms, name='washrooms'),
    path('faucets', views.faucets, name='faucets'),
    path('media', views.media, name='media'),
    path('reporting', views.reporting, name='reporting'),
    path('user-admin', views.user_admin, name='user_admin'),
    path('avno-admin', views.avno_admin, name='avno_admin'),
    path('profile', views.profile, name='profile'),
]
