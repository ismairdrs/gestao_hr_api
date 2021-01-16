from django.urls import path, include
from .views import EmpresaCreateView, EmpresaListView, EmpresaUpdateView

urlpatterns = [
    path('', EmpresaListView.as_view(), name='list_empresas'),
    path('nova', EmpresaCreateView.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', EmpresaUpdateView.as_view(), name='update_empresa'),

]
