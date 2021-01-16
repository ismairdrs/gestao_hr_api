from django.urls import path
from .views import (
    DepartamentosList,
    DepartamentoCreate,
    DepartamentoUpdate,
    DepartamentoDeletar
)

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentoUpdate.as_view(), name='update_departamento'),
    path('deletar/<int:pk>', DepartamentoDeletar.as_view(), name='delete_departamento'),

]
