from django.core.exceptions import ValidationError


def valida_cep(value):
    import re
    cep = re.compile('^[0-9]{8}$')
    if cep.match(value) is None:
        raise ValidationError('CEP deve possuir 8 dígitos.')


def valida_telefone(value):
    import re
    telefone = re.compile('^[1-9][1-9][0-9]{8,9}$')
    if telefone.match(value) is None:
        raise ValidationError('Telefone deve ser no formato DDD + Número.')
