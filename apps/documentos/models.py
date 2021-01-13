from django.db import models


class Documento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()