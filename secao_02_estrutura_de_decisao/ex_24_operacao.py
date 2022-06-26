"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    soma = n_1 + n_2
    subtracao = n_1 - n_2
    divisao = n_1 / n_2
    multiplicacao = n_1 * n_2

    if operacao == '+':
        resultado = float(soma)
        if resultado.is_integer() and resultado % 2 == 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, positivo e inteiro.')
        elif resultado.is_integer() and resultado % 2 == 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, negativo e inteiro.')
        elif resultado.is_integer() and resultado % 2 != 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, positivo e inteiro.')
        elif resultado.is_integer() and resultado % 2 != 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, negativo e inteiro.')
        elif resultado.is_integer() and resultado == 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, neutro e inteiro.')
        elif resultado % 2 == 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, positivo e decimal.')
        elif resultado % 2 == 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, negativo e decimal.')
        elif resultado % 2 != 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, positivo e decimal.')
        elif resultado % 2 != 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, negativo e decimal.')

    if operacao == '/':
        resultado = float(divisao)
        if resultado.is_integer() and resultado % 2 == 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, positivo e inteiro.')
        elif resultado.is_integer() and resultado % 2 == 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, negativo e inteiro.')
        elif resultado.is_integer() and resultado % 2 != 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, positivo e inteiro.')
        elif resultado.is_integer() and resultado % 2 != 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, negativo e inteiro.')
        elif resultado.is_integer() and resultado == 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, neutro e inteiro.')
        elif resultado % 2 == 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, positivo e decimal.')
        elif resultado % 2 == 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, negativo e decimal.')
        elif resultado % 2 != 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, positivo e decimal.')
        elif resultado % 2 != 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, negativo e decimal.')

    if operacao == '-':
        resultado = float(subtracao)
        if resultado.is_integer() and resultado % 2 == 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, positivo e inteiro.')
        elif resultado.is_integer() and resultado % 2 == 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, negativo e inteiro.')
        elif resultado.is_integer() and resultado % 2 != 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, positivo e inteiro.')
        elif resultado.is_integer() and resultado % 2 != 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, negativo e inteiro.')
        elif resultado.is_integer() and resultado == 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, neutro e inteiro.')
        elif resultado % 2 == 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é positivo e decimal.')
        elif resultado % 2 == 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, negativo e decimal.')
        elif resultado % 2 != 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é positivo e decimal.')
        elif resultado % 2 != 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, negativo e decimal.')

    if operacao == '*':
        resultado = float(multiplicacao)
        if resultado.is_integer() and resultado % 2 == 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, positivo e inteiro.')
        elif resultado.is_integer() and resultado % 2 == 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, negativo e inteiro.')
        elif resultado.is_integer() and resultado % 2 != 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, positivo e inteiro.')
        elif resultado.is_integer() and resultado % 2 != 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, negativo e inteiro.')
        elif resultado.is_integer() and resultado == 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, neutro e inteiro.')
        elif resultado % 2 == 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, positivo e decimal.')
        elif resultado % 2 == 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é par, negativo e decimal.')
        elif resultado % 2 != 0 and resultado > 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é impar, positivo e decimal.')
        elif resultado % 2 != 0 and resultado < 0:
            print(f'Resultado: {resultado:.2f}')
            print('Número é negativo e decimal.')
        elif resultado == 0:
            print(f'Resultado: {resultado}')
            print('Número é par, neutro e inteiro.')
            
