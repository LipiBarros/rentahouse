from django.core.exceptions import ValidationError


def valida_cep(value):
    import re
    cep = re.compile('^[0-9]{8}$')
    if cep.match(value) is None:
        raise ValidationError('CEP deve possuir 8 dígitos.')
