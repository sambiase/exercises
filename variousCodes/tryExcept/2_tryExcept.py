
numero = int(input('Digite um numero --> '))
try:
    print(f'\nNumero digitado --> {numero}')
except:
    raise ValueError('Ocorreu um erro')
