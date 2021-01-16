from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .models import RegistroHoraExtra


class RegistroHoraExtraList(ListView):
    model = RegistroHoraExtra


class RegistroHoraExtraCreate(CreateView):
    medel = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas','utilizada']


class RegistroHoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_funcionarios')
