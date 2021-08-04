'''
    Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

lista = []

for i in range(5):
    lista.append(i)

print(f'Lista --> {lista}')
print(f'ID da lista --> {id(lista)}')
print(f'Tipo do objeto --> {type(lista)}')

