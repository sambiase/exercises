'''
    Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = str(input('Digite uma Letra: '))

lst_todas_as_vogais = ['a','e','i','o','u']

if letra in lst_todas_as_vogais:
    print(f'Letra digitada eh uma vogal')
else:
    print(f'Letra digitada nao eh uma vogal')




