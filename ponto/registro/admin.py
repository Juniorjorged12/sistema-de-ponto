from django.contrib import admin
from .models import Empresa, Funcionario, RegistroPonto

admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(RegistroPonto)