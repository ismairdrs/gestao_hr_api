from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('registro_hora_extra/', include('apps.registro_hora_extra.urls')),
    path('', include('apps.core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
