'''
    Faça um Programa que leia três números e mostre o maior deles.
'''

n1 = int(input('Digite o Numero 1: '))
n2 = int(input('Digite o Numero 2: '))
n3 = int(input('Digite o Numero 3: '))

lst = [n1,n2,n3]
lst.sort()
print(lst[2])
