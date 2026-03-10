from django.urls import path
from . import views

urlpatterns = [
    path("entrada/<int:funcionario_id>/", views.registrar_entrada, name="entrada"),
    path("saida/<int:funcionario_id>/", views.registrar_saida, name="saida"),
]