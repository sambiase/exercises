'''
    Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

lista = []
lista_vogais = ['a','e','i','o','u']

for i in range(10):
    char = str(input(f'Digite {i}o char --> '))
    lista.append(char)

print(lista)
