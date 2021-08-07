'''
     Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
     dezenas e unidades do mesmo.

            Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

                326 = 3 centenas, 2 dezenas e 6 unidades
                12 = 1 dezena e 2 unidades

                Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

numero = 121

if numero < 1000:
    numero_string = str(numero)
    if len(numero_string) == 3:
        print(f'{numero_string[0]} centenas, {numero_string[1]} dezenas e {numero_string[2]} unidades')
    elif len(numero_string) == 2:
        print(f'{numero_string[0]} dezena e {numero_string[1]} unidades')
    else:
        print(f'{numero_string[0]} unidades')
else:
    print('Numero nao pode ser maior do que 1000')
