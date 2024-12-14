# ....Mouhamadou Bamba Dieng ... 2024  Horus Global Services ...
# ..... +221 77 249 05 30 bigrip2016@gmail.com ....

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import (
    VehiculeCreateView,
    VehiculeUpdateView,
    VehiculeDeleteView,
    VehiculeListView,
)

handler404 = 'horusapp.views.custom_page_not_found_view'

urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),

    # Authentification
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Gestion générale
    path('horusapp/', views.gestion, name='horusapp'),

    # Gestion des véhicules
    path('vehicules/', VehiculeListView.as_view(), name='vehicule_list'),
    path('vehicule/ajouter/', VehiculeCreateView.as_view(), name='vehicule_create'),
    path('vehicule/modifier/<int:pk>/', VehiculeUpdateView.as_view(), name='vehicule_update'),
    path('vehicule/supprimer/<int:pk>/', VehiculeDeleteView.as_view(), name='vehicule_delete'),

    # Fonctionnalité de recherche
    path('search/', views.search, name='search'),

    # Exportation des véhicules
    path('export/csv/', views.export_vehicules_csv, name='export_vehicules_csv'),
    path('export/vehicules/pdf/', views.export_vehicules_pdf, name='export_vehicules_pdf'),
]
