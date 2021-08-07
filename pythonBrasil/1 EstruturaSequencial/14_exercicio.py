'''
   João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
   Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
   São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um
   programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
   de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa
   com as mensagens adequadas.
'''

peso_de_peixes = float(input('Peso do Peixe --> '))

if peso_de_peixes > 50:
    excesso_peso = peso_de_peixes - 50
    multa = excesso_peso * 4
    print(f'Excesso de Peso --> {excesso_peso}')
    print(f'Multa --> R$ {multa}')
else:
    print(f'Nao houve excesso e nem multa :)')