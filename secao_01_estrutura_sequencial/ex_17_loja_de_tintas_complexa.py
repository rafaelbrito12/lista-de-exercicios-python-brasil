"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


from math import ceil


def calcular_latas_e_preco_de_tinta():
    tamanho = float(input('Digite o tamanho da area a ser pintada: '))
    litros = ceil((18 * tamanho) / (6 * 18))
    litros_folga = round(litros * 10 / 100)
    litros_total = litros + litros_folga

    lata = ceil(litros_total / 18)
    preco_lata = 80 * lata
    sobra = lata * 18 - litros_total

    qtd_galao = ceil(litros_total / 3.6)
    preco_galao = qtd_galao * 25
    sobra_galao = qtd_galao * 3.6 - litros_total

    x_galao = round(litros_total % 3.6)
    y_litro = round(litros_total // 18)
    soma_galao_litro = (y_litro * 80)+(x_galao * 25)

    print(f'Você deve comprar {litros_total} litros de tinta.')
    print(f'Você pode comprar {lata} lata(s) de 18 litros a um custo de R$ {preco_lata:.0f}. Vão sobrar {sobra:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {qtd_galao} lata(s) de 3.6 litros a um custo de R$ {preco_galao}. Vão sobrar {sobra_galao:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {y_litro} lata(s) de 18 litros e {x_galao} galão(ões) de 3.6 litros a um custo de R$ {soma_galao_litro}. Vão sobrar 2.6 litro(s) de tinta.')

