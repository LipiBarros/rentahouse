from django.db import models
from .validators import valida_cep


class Imovel(models.Model):

    TIPO_CHOICES = (
        ('AP', 'Apartamento'),
        ('CS', 'Casa'),
        ('CF', 'Condomínio fechado'),
        ('SB', 'Sobrado')
    )
    QUARTO_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 ou mais')
    )

    UF_CHOICES = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AP', 'AP'),
        ('AM', 'AM'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('MG', 'MG'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PR', 'PR'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RS', 'RS'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('SC', 'SC'),
        ('SP', 'SP'),
        ('SE', 'SE'),
        ('TO', 'TO'),
    )
    
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, null=False, blank=False)
    qt_quartos = models.PositiveIntegerField(choices=QUARTO_CHOICES, blank=False)
    area = models.PositiveIntegerField(null=True, blank=True)
    qt_vagas_garagem = models.PositiveIntegerField(null=False, blank=False)
    vl_aluguel = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    cep = models.CharField(max_length=9, null=False, blank=False, validators=[valida_cep])
    logradouro = models.CharField(max_length=80, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    municipio = models.CharField(max_length=50, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True, choices=UF_CHOICES)
    telefone = models.CharField(max_length=15, null=False, blank=True)
    dh_insercao = models.DateTimeField(auto_now_add=True)
    dh_alteracao = models.DateTimeField(auto_now=True)
    foto = models.FileField(null=True, blank=True, upload_to='anuncios/%Y/%m/%d/')


