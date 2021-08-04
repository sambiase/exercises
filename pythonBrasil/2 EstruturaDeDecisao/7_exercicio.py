'''
    Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

n1 = int(input('Digite o Numero 1: '))
n2 = int(input('Digite o Numero 2: '))
n3 = int(input('Digite o Numero 3: '))

lst = [n1,n2,n3]
lst.sort()
print(f'Maior numero: {lst[2]}')
print(f'Menor numero: {lst[0]}')

