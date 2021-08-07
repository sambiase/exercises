'''
   Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
   ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
   vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
   compradas e o preço total.
'''

area = float(input('Tamanho em m2 da area a ser pintada --> '))
litros = area / 3

if litros <= 18:
    print('Latas de Tintas a serem compradas --> 1')
    print('Preço Total: R$ 80')
else:
    qtd_latas = litros / 18
    preço_total = qtd_latas * 80
    print(f'Latas de Tintas a serem compradas --> {round(qtd_latas,2)}')
    print(f'Preço Total --> R$ {round(preço_total,2)}')


