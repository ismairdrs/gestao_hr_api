from django.contrib import admin
from .models import Departamento


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'empresa')


admin.site.register(Departamento, DepartamentoAdmin)
