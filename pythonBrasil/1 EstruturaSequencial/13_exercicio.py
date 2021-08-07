'''
   Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
   utilizando as seguintes fórmulas:

        Para homens: (72.7*h) - 58
        Para mulheres: (62.1*h) - 44.7
'''

altura = float(input('Altura --> '))
sexo = str(input('(H)omem ou (M)ulher ? --> '))

if sexo.upper() == 'H':
    peso_ideal = (72.7 * altura) - 58
    print(f'Homem - Peso Ideal --> {peso_ideal}')
elif sexo.upper() == 'M':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Mulher - Peso Ideal --> {peso_ideal}')
else:
    print('Sexo Invalido')
