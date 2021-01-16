from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo',]


class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_documentos')
