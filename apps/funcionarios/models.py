from django.contrib.auth.models import User
from django.db import models
from apps.empresas.models import Empresa
from apps.departamentos.models import Departamento


class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
