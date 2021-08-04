'''
   Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números
'''

import math

lista = [int(i) for i in range(5, 7)]
soma = 0
for i in lista:
    soma += i

mult_res_lista = lambda self: math.prod(lista)
print(f'Lista: {lista}')
print(f'Soma: {soma}')
print(f'Multiplicacao: {mult_res_lista(None)}')
