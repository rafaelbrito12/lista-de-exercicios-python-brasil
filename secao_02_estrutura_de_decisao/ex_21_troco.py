"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    sobra = valor
    tipo_nota = []

    while sobra > 0:

        if valor // 100 != 0:
            notas_100 = valor // 100
            sobra = valor - (notas_100 * 100)
            valor = sobra
            if notas_100 > 1:
                tipo_nota.append(f'{notas_100} notas de R$ 100')
            else:
                tipo_nota.append(f'{notas_100} nota de R$ 100')
        elif valor // 50 != 0:
            notas_50 = valor // 50
            sobra = valor - (notas_50 * 50)
            valor = sobra
            if notas_50 > 1:
                tipo_nota.append(f'{notas_50} notas de R$ 50')
            else:
                tipo_nota.append(f'{notas_50} nota de R$ 50')
        elif valor // 10 != 0:
            notas_10 = valor // 10
            sobra = valor - (notas_10 * 10)
            valor = sobra
            if notas_10 > 1:
                tipo_nota.append(f'{notas_10} notas de R$ 10')
            else:
                tipo_nota.append(f'{notas_10} nota de R$ 10')
        elif valor // 5 != 0:
            notas_5 = valor // 5
            sobra = valor - (notas_5 * 5)
            valor = sobra
            if notas_5 >= 2:
                tipo_nota.append(f'{notas_5} notas de R$ 5')
            else:
                tipo_nota.append(f'{notas_5} nota de R$ 5')
        elif valor // 1 != 0:
            notas_1 = valor // 1
            sobra = valor - (notas_1 * 1)
            if notas_1 > 1:
                tipo_nota.append(f'{notas_1} notas de R$ 1')
            else:
                tipo_nota.append(f'{notas_1} nota de R$ 1')

    if len(tipo_nota) == 1:
        return ', '.join(tipo_nota)
    if len(tipo_nota) == 2:
        return ' e '.join(tipo_nota)
    if len(tipo_nota) == 3:
        return f'{tipo_nota[0]}, {tipo_nota[1]} e {tipo_nota[2]}'
    if len(tipo_nota) == 4:
        return f'{tipo_nota[0]}, {tipo_nota[1]}, {tipo_nota[2]} e {tipo_nota[3]}'
    if len(tipo_nota) == 5:
        return f'{tipo_nota[0]}, {tipo_nota[1]}, {tipo_nota[2]}, {tipo_nota[3]} e {tipo_nota[4]}'