'''
   Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
   Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
   Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

        salário bruto.
        quanto pagou ao INSS.
        quanto pagou ao sindicato.
        o salário líquido.
        calcule os descontos e o salário líquido, conforme a tabela abaixo:

        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$

        Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

ganhos_por_hora = float(input('Ganhos por Hora --> '))
nr_horas_trabalhadas_mes = float(input('Numero de Horas Trabalhadas por Mes --> '))

salario_bruto = ganhos_por_hora * nr_horas_trabalhadas_mes
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print(f'\n+ Salário Bruto : R$ {salario_bruto}')
print(f'- IR (11%) : R$ {imposto_renda}')
print(f'- INSS (8%) : R$ {inss}')
print(f'- Sindicato ( 5%) : R$ {sindicato}')
print(f'= Salário Liquido : R$ {salario_liquido}')
