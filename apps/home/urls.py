from django.urls import path, re_path
from apps.home import views

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
]
