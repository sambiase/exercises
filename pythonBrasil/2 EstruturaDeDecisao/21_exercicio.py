'''
     Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e
     depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100
     reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade
     de notas existentes na máquina.

        Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
        uma nota de 5 e uma nota de 1;

        Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
        quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

#valor_saque = float(input('Digite o valor de saque --> R$ '))

valor_saque = 256


if valor_saque < 10 or valor_saque > 600:
    print('Valor minimo é de R$ 10 e Valor maximo é de R$ 600')
else:
    valor_centena = valor_saque // 100
