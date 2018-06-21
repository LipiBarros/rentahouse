from unicodedata import normalize


def remover_espaco_duplo(texto):
    espaco = ' '
    while 2 * espaco in texto:
        texto = texto.replace(2 * espaco, espaco)
    return texto


def remover_acentos(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


def manter_digitos(numero):
    return ''.join([digito for digito in numero if digito.isdigit()])
