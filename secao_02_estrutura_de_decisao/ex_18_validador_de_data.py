"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    if len(data) >= 5:
        nova_data = data.split('/')
        dia, mes, ano = nova_data

        if int(dia) <= 0 or int(mes) < 1 or int(mes) > 12 or int(ano) <= 0:
            return 'Data inválida'
        elif int(mes) == 2 and int(dia) > 29:
            return 'Data inválida'
        elif int(dia) in range(31) and int(mes) in range(13) and int(ano) > 0:
            return 'Data válida'
    else:
        return 'Data inválida'

