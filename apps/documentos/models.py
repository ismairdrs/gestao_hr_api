from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.TextField()
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.descricao
