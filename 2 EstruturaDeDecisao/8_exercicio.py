'''
    Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
    sabendo que a decisão é sempre pelo mais barato.
'''

preco_produto1 = float(input('Preco do Produto 1: '))
preco_produto2 = float(input('Preco do Produto 2: '))
preco_produto3 = float(input('Preco do Produto 3: '))

if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
    print('Produto 1 eh o mais barato')
elif preco_produto2 < preco_produto1 and preco_produto2 < preco_produto3:
    print('Produto 2 eh o mais barato')
elif preco_produto3 < preco_produto1 and preco_produto3 < preco_produto1:
    print('Produto 3 eh o mais barato')
else:
    print('Os 3 produtos tem o mesmo valor')



