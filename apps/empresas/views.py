from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Empresa


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ('nome', )

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')


class EmpresaListView(ListView):
    model = Empresa


class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ('nome', )
