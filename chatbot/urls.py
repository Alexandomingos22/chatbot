from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('capturas/', include('capturas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('perguntas/', include('perguntas.urls')),
    path('tela/', include('home.urls')),
    path('home/opcao/', include('home.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)