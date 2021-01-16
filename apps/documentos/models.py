from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.TextField()
    #pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolunte_url(self):
        return reverse('update_funcionario', args=(self.pertence.id))


    def __str__(self):
        return self.descricao
