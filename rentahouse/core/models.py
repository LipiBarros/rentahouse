from django.db import models
from .validators import valida_cep


class Imovel(models.Model):

    TIPO_CHOICES = (
        ('P', 'Padrão'),
        ('V', 'Vila'),
        ('CF', 'Condomínio fechado')
    )
    QUARTO_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 ou mais')
    )
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, null=False, blank=False)
    qt_quartos = models.PositiveIntegerField(choices=QUARTO_CHOICES, blank=False)
    area = models.PositiveIntegerField(null=True, blank=True)
    qt_vagas_garagem = models.PositiveIntegerField(default=0, null=False, blank=True)
    vl_condominio = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=True, default=0.00)
    vl_aluguel = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    cep = models.CharField(max_length=9, null=False, blank=False, validators=[valida_cep])
    endereco = models.CharField(max_length=250, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=False, blank=True)
    email = models.EmailField(max_length=60, null=True, blank=True)
    dh_insercao = models.DateTimeField(auto_now_add=True)
    dh_alteracao = models.DateTimeField(auto_now=True)


