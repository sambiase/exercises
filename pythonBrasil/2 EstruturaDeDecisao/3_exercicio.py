'''
    Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

letra = str(input('Digite uma Letra: '))

if letra.upper() == 'F':
    print(f'F - Feminino')
elif letra.upper() == 'M':
    print(f'M - Masculino')
else:
    print(f'Sexo Invalido')


