"""
ASGI config for Systemflix project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Systemflix.settings')

application = get_asgi_application()


from django.db import models

# Create your models here.

FORMA_DE_PAGAMENTO_CHOICES = (
    ("DEBITO", "Débito"),
    ("CRÉDITO", "Crédito"),
    ("DINHEIRO", "Dinheiro")
)

FECHAR_VENDA_CHOICES = (
    ("NOTA DE PEDIDO", "Nota de pedido"),
    ("NOTA FISCAL", "Nota fiscal")
)

VALOR_TOTAL_VENDAS_CHOICES = (
    ("DIARIO", "Diário"),
    ("SEMANAL", "Semanal"),
    ("QUINZENAL", "Quinzenal"),
    ("MENSAL", "Mensal")
)



ESTADO_CHOICES = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espirito Santo"),
    ("GO", "Goias"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piaui"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", " Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins")
)



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cnpj_cpf = models.CharField(max_length=14)
    fone = models.CharField(max_length=11)
    email = models.EmailField(null=False, unique=True)


    def __str__(self):
        return self.nome


