"""
Exercício 27 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o
valor a ser pago pelo cliente.
Mostre o restultado com duas casas decimais

    >>> calcular_preco_da_compra(2, 0)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  5.00
    >>> calcular_preco_da_compra(6, 0)
    (+)  Morango  - valor:  R$ 13.20 - quantidade:  6 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$ 13.20
    >>> calcular_preco_da_compra(9, 0)
    (+)  Morango  - valor:  R$ 19.80 - quantidade:  9 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  1.98
              Valor Total:  R$ 17.82
    >>> calcular_preco_da_compra(0, 2)
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  3.60
    >>> calcular_preco_da_compra(0, 6)
    (+)  Maça     - valor:  R$  9.00 - quantidade:  6 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  9.00
    >>> calcular_preco_da_compra(0, 9)
    (+)  Maça     - valor:  R$ 13.50 - quantidade:  9 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  1.35
              Valor Total:  R$ 12.15
    >>> calcular_preco_da_compra(2, 2)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  8.60
    >>> calcular_preco_da_compra(7, 2)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  1.90
              Valor Total:  R$ 17.10
    >>> calcular_preco_da_compra(7, 7)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$ 10.50 - quantidade:  7 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  2.59
              Valor Total:  R$ 23.31

"""


def calcular_preco_da_compra(kilos_de_morango: int, kilos_de_maca: int):
    kg_total = kilos_de_morango + kilos_de_maca
    valor_total = (kilos_de_morango * 2.50) + (kilos_de_maca * 1.80)
    if kilos_de_morango and kilos_de_maca:
        if (kilos_de_morango <= 5 and kilos_de_maca <= 5) and kg_total < 8 and valor_total < 25:
            valor_morango = (kilos_de_morango * 2.50)
            valor_maca = (kilos_de_maca * 1.80)
            valor_a_pagar = valor_morango + valor_maca
            print(
             f'(+)  Morango  - valor:  R$  {valor_morango:.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ 2.50/kg')
            print(
             f'(+)  Maça     - valor:  R$  {valor_maca:.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ 1.80/kg')
            print(f'(-)  Desconto - valor:  R$  0.00')
            print(f'          Valor Total:  R$  {valor_a_pagar:.2f}')

        elif (kilos_de_morango <= 5 and kilos_de_maca > 5) and kg_total < 8 and valor_total < 25:
            valor_morango = (kilos_de_morango * 2.20)
            valor_maca = (kilos_de_maca * 1.50)
            valor_a_pagar = (valor_morango + valor_maca)
            print(f'(+)  Morango  - valor:  R$ {valor_morango:.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ 2.20/kg')
            print(f'(+)  Maça     - valor:  R$ {valor_maca:.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ 1.50/kg')
            print(f'(-)  Desconto - valor:  R$  0.00')
            print(f'          Valor Total:  R$ {valor_a_pagar:.2f}')

        elif (kilos_de_morango > 5 and kilos_de_maca <= 5) and kg_total < 8 and valor_total < 25:
            valor_morango = (kilos_de_morango * 2.50)
            valor_maca = (kilos_de_maca * 1.50)
            valor_a_pagar = (valor_morango + valor_maca)
            print(f'(+)  Morango  - valor:  R$ {valor_morango:.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ 2.20/kg')
            print(f'(+)  Maça     - valor:  R$  {valor_maca:.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ 1.50/kg')
            print(f'(-)  Desconto - valor:  R$  0.00')
            print(f'          Valor Total:  R$ {valor_a_pagar:.2f}')

        elif (kilos_de_morango > 5 and kilos_de_maca <= 5) and (kg_total > 8 or valor_total < 25):
            valor_morango = (kilos_de_morango * 2.20)
            valor_maca = (kilos_de_maca * 1.80)
            desconto = ((valor_morango + valor_maca) * 10) / 100
            valor_a_pagar = (valor_morango + valor_maca) - desconto
            print(f'(+)  Morango  - valor:  R$ {valor_morango:.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ 2.20/kg')
            print(f'(+)  Maça     - valor:  R$  {valor_maca:.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ 1.80/kg')
            print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
            print(f'          Valor Total:  R$ {valor_a_pagar:.2f}')

        elif (kilos_de_morango > 5 and kilos_de_maca > 5) and kg_total >= 8 or valor_total >= 25:
            valor_morango = (kilos_de_morango * 2.20)
            valor_maca = (kilos_de_maca * 1.50)
            desconto = ((valor_morango + valor_maca) * 10) / 100
            valor_a_pagar = (valor_morango + valor_maca) - desconto
            print(f'(+)  Morango  - valor:  R$ {valor_morango:.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ 2.20/kg')
            print(f'(+)  Maça     - valor:  R$ {valor_maca:.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ 1.50/kg')
            print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
            print(f'          Valor Total:  R$ {valor_a_pagar:.2f}')

    if kilos_de_morango and not kilos_de_maca:
        if kilos_de_morango <= 5:
            valor_morango = (kilos_de_morango * 2.50)
            print(f'(+)  Morango  - valor:  R$  {valor_morango:.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ 2.50/kg')
            print(f'(-)  Desconto - valor:  R$  0.00')
            print(f'          Valor Total:  R$  {valor_morango:.2f}')

        elif kilos_de_morango > 5 and kg_total < 8:
            valor_morango = (kilos_de_morango * 2.20)
            total = valor_morango
            print(f'(+)  Morango  - valor:  R$ {valor_morango:.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ 2.20/kg')
            print(f'(-)  Desconto - valor:  R$  0.00')
            print(f'          Valor Total:  R$ {total:.2f}')
        elif kilos_de_morango > 5 and kg_total >= 8:
            valor_morango = (kilos_de_morango * 2.20)
            desconto = (valor_morango * 10) / 100
            total = valor_morango - desconto
            print(f'(+)  Morango  - valor:  R$ {valor_morango:.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ 2.20/kg')
            print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
            print(f'          Valor Total:  R$ {total:.2f}')

    if not kilos_de_morango and kilos_de_maca:
        if kilos_de_maca <= 5:
            valor_maca = (kilos_de_maca * 1.80)
            print(f'(+)  Maça     - valor:  R$  {valor_maca:.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ 1.80/kg')
            print(f'(-)  Desconto - valor:  R$  0.00')
            print(f'          Valor Total:  R$  {valor_maca:.2f}')
        elif kilos_de_maca > 5 and kg_total < 8:
            valor_maca = (kilos_de_maca * 1.50)
            total = valor_maca
            print(f'(+)  Maça     - valor:  R$  {valor_maca:.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ 1.50/kg')
            print(f'(-)  Desconto - valor:  R$  0.00')
            print(f'          Valor Total:  R$  {total:.2f}')
        elif kilos_de_maca > 5 and kg_total >= 8:
            valor_maca = (kilos_de_maca * 1.50)
            desconto = (valor_maca * 10) / 100
            total = valor_maca - desconto
            print(f'(+)  Maça     - valor:  R$ {valor_maca:.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ 1.50/kg')
            print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
            print(f'          Valor Total:  R$ {total:.2f}')

