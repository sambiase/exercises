'''
    Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

lista = []
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))
nota4 = int(input('Nota 4: '))
lista.extend([nota1,nota2,nota3,nota4])

for i,v in enumerate(lista):
    print(f'Nota {i} --> {v}')
