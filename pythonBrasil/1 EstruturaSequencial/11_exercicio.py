'''
   Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

        o produto do dobro do primeiro com metade do segundo .
        a soma do triplo do primeiro com o terceiro.
        o terceiro elevado ao cubo.
'''
import math as mate

n1_int = int(input('Digite o 1o numero Inteiro --> '))
n2_int = int(input('Digite o 2o numero Inteiro --> '))
n3_float = float(input('Digite o um numero Real --> '))

res_prod = (2 * n1_int) * (2 / n2_int)
soma = (3 * n1_int) + n3_float
elevado = mate.pow(n3_float, 3)

print(f'Produto do dobro do primeiro com metade do segundo --> {res_prod}')
print(f'Soma do triplo do primeiro com o terceiro --> {soma}')
print(f'Terceiro elevado ao cubo --> {elevado}')
