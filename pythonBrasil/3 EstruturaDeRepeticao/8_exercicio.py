'''
   Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

soma = 0
media = 0

for i in range(5):
    numero = float(input(f'Digite o numero {i+1}-->  '))
    soma += numero

media = soma / 5

print (f'Soma dos numeros: {soma}')
print (f'Media dos numeros: {media}')