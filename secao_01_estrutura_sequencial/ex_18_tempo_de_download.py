"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos

    >>> from secao_01_estrutura_sequencial import ex_18_tempo_de_download
    >>> numeros =['50', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 7 minuto(s)
    >>> numeros =['100', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 3 minuto(s)

"""


def calcular_tempo_de_download():
    tamanho_arquivo = float(input('digite o tamanho do arquivo em MB: '))
    transferencia = float(input('Digite a velocidade de um link de Internet (em Mbps): '))

    transf_kb = round((transferencia * 1024) / 8)
    tamanho_kb = round(tamanho_arquivo * 1024)
    tempo = round((tamanho_kb / transf_kb) / 60)
    print(f'O tempo aproximado do Download é: {tempo} minuto(s)')




