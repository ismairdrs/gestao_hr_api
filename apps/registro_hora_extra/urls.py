from django.urls import path
from .views import RegistroHoraExtraList

urlpatterns = [

    path('', RegistroHoraExtraList.as_view(), name='list_horas_extras'),
]
