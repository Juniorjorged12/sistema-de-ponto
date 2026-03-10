
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Funcionario, RegistroPonto

def registrar_entrada(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    registro = RegistroPonto.objects.create(funcionario=funcionario, entrada=datetime.now())
    return JsonResponse({"status": "entrada registrada", "hora": registro.entrada})


def registrar_saida(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    registro = funcionario.registros.filter(saida__isnull=True).last()
    if registro:
        registro.saida = datetime.now()
        registro.save()
        return JsonResponse({"status": "saida registrada", "hora": registro.saida})
    return JsonResponse({"status": "nenhuma entrada encontrada"})
