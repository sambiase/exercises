'''
    Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
n3 = int(input('Digite o numero 3: '))

lst = [n1, n2, n3]
lst.sort()
lst.reverse()
print(f'{lst}')



