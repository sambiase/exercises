'''
    Faça um Programa que leia um número e exiba o dia correspondente da semana.
    (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

dias_da_semana = {1: 'Domingo', 2: 'Segunda', 3: 'Terca', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}
dia = int(input('Digite um numero de 1 a 7 \n'))

if dia in dias_da_semana.keys():
    print(f'Dia da semana correspondente: {dias_da_semana.get(dia)}')
else:
    print(f'Valor invalido')

