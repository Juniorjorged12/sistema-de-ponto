from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="funcionarios")
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome


class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="registros")
    entrada = models.DateTimeField(null=True, blank=True)
    saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.funcionario.nome} - {self.entrada} / {self.saida}"