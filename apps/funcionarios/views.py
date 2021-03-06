from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import Funcionario


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ('nome', 'departamentos',)

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + str(funcionario.id)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ('nome', 'departamentos')


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')
