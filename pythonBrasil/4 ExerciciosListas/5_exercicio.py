'''
    Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no
    vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''


lista = [int(i) for i in range(20)]
lista_pares = []
lista_impares = []

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print(f'Lista: {lista}')
print(f'Lista Par: {lista_pares}')
print(f'Lista Impar: {lista_impares}')
