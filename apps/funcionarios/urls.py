from django.urls import path, include
from .views import FuncionarioList, FuncionarioUpdate, FuncionarioDelete, FuncionarioCreate

urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionarioUpdate.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
]
