'''
   Faça um programa que leia 5 números e informe o maior número.
'''

maximo = float(input('Digite 1 numero --> '))

for _ in range(5):
    numero_max = max(maximo,float(input('Digite 1 numero --> ')))
    print(f'Numero max encontrado ate o momento é --> {numero_max}')


