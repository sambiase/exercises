import math
import math as mate

'''
   Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
   pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
   em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

        Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
            comprar apenas latas de 18 litros;
            comprar apenas galões de 3,6 litros;
            misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
            arredonde os valores para cima, isto é, considere latas cheias.
'''

area = float(input('Tamanho em m2 da area a ser pintada --> '))
area_com_folga = area * 1.1
litros = area_com_folga / 6
numero_de_latas = litros / 18
print (f'Litros a serem usados --> {litros}')
print (f'Numero de latas --> {numero_de_latas}')
print (f'Arrendondar para cima --> {math.ceil(numero_de_latas)}')



