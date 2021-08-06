'''
    Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
    Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

        Compara duas strings
        String 1: Brasil Hexa 2006
        String 2: Brasil! Hexa 2006!
        Tamanho de "Brasil Hexa 2006": 16 caracteres
        Tamanho de "Brasil! Hexa 2006!": 18 caracteres
        As duas strings são de tamanhos diferentes.
        As duas strings possuem conteúdo diferente.
'''

str_1 = str(input('1a String --> '))
str_2 = str(input('2a String --> '))

print(f'Tamanho de {str_1}: {len(str_1)} caracteres')
print(f'Tamanho de {str_2}: {len(str_2)} caracteres')

if len(str_1) != len(str_2):
    print('As duas strings são de tamanhos diferentes.')

if str_1 != str_2:
    print('As duas strings possuem conteúdo diferente.')