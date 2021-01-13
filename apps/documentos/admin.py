from django.contrib import admin
from .models import Documento


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nome', )


admin.site.register(Documento, DocumentoAdmin)
