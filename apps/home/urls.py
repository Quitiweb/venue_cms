from django.urls import path
from apps.home import views, views_api

urlpatterns = [
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

    path('', views.index, name='home'),
    path('show/<str:model>', views.show, name='show_model'),
    path('add/<str:model>/new_record', views.create_new_record, name='add_new_record'),
    path('delete/<str:model>/<int:pk>', views.delete, name='delete_model'),
    path('update/<str:model>/<int:pk>', views.update, name='update_model'),
    path('reporting', views.reporting, name='reporting'),
    path('profile', views.profile, name='profile'),

    # endpoints
    path('get_washrooms/<int:venue>', views_api.get_washrooms, name='get_washrooms'),
    path('api/login', views_api.api_login, name='api_login'),
    path('api/get_date', views_api.api_get_date, name='api_get_date'),
    path('api/get_playlist', views_api.api_get_playlist, name='api_get_playlist'),
]
