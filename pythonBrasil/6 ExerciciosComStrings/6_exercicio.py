'''
   Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a
   data com o nome do mês por extenso.

        Data de Nascimento: 29/10/1973
        Você nasceu em  29 de Outubro de 1973.
'''
import calendar

dia = '18'
mes = 2
ano = '1979'

print(f'Data de Nascimento: {dia}/{mes}/{ano}')
print(f'Voce nasceu em {dia} de {calendar.month_name[mes]} de {ano}')