from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),             # Route pour l'administration
    path('gestion/', include('horusapp.urls')),  # Inclut les URLs de mon application
    path('', include('horusapp.urls')),          # Route par défaut pour l'application
]

# Ajouter les configurations pour servir les fichiers statiques et médias
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Utilisation de STATIC_ROOT
