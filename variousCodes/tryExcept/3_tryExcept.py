'''
    try except sem o uso do raise
'''

try:
    numero = int(input('Digite um numero inteiro --> '))
except ValueError:
    print('Nao é um inteiro')

