from django.contrib import admin
from .models import Departamento


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Departamento, DepartamentoAdmin)
