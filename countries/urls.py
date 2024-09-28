from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('countries/create/', views.country_create, name='country_create'),
    path('countries/update/<int:pk>/', views.country_update, name='country_update'),
    path('countries/delete/<int:pk>/', views.country_delete, name='country_delete'),
    path('countries/archive/<int:pk>/', views.country_archive, name='country_archive'),
    path('countries/restore/archive/<int:pk>/', views.country_restore_archive, name='country_restore_archive'),
    path('country/toggle-status/<int:pk>/', views.toggle_country_status, name='country_status'),
    path('archived-countries/', views.archived_country_list, name='archived_countries'),
    path('countries/<int:pk>/', views.country_detail, name='country_detail'),

    path('cities/create/', views.city_create, name='city_create'),
    path('cities/toggle-status/<int:pk>/', views.toggle_city_status, name='city_status'),
    path('cities/update/<int:pk>/', views.city_update, name='city_update'),
    path('cities/delete/<int:pk>/', views.city_delete, name='city_delete'),
    path('cities/archive/<int:pk>/', views.city_archive, name='city_archive'),
    path('cities/unarchive/<int:pk>/', views.city_restore_archive, name='city_restore'),
]
