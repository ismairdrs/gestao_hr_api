from django.contrib import admin
from .models import RegistroHoraExtra


class RegistroHoraExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'motivo', 'funcionario')


admin.site.register(RegistroHoraExtra, RegistroHoraExtraAdmin)
