'''
    Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
    são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
    e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
    O Salário Líquido corresponde ao Salário Bruto menos os descontos.
    O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

        Desconto do IR:
        Salário Bruto até 900 (inclusive) - isento
        Salário Bruto até 1500 (inclusive) - desconto de 5%
        Salário Bruto até 2500 (inclusive) - desconto de 10%
        Salário Bruto acima de 2500 - desconto de 20%

        Imprima na tela as informações, dispostas conforme o exemplo abaixo.
        No exemplo o valor da hora é 5 e a quantidade de hora é 220.

                Salário Bruto: (5 * 220)        : R$ 1100,00
                (-) IR (5%)                     : R$   55,00
                (-) INSS ( 10%)                 : R$  110,00
                FGTS (11%)                      : R$  121,00
                Total de descontos              : R$  165,00
                Salário Liquido                 : R$  935,00
'''

valor_hora = float(input('Informe o valor hora de trabalho: R$ '))
qtd_horas_trabalhadas_mes = float(input('Informe a quantidade de horas trabalhadas no mes: '))
salario_bruto = valor_hora * qtd_horas_trabalhadas_mes

if salario_bruto <= 900:
    pass
elif 900 < salario_bruto <= 1500:
    imposto_de_renda = salario_bruto * 0.05
    percentual_ir = '5%'
elif 1500 < salario_bruto <= 2500:
    imposto_de_renda = salario_bruto * 0.1
    percentual_ir = '10%'
else:
    imposto_de_renda = salario_bruto * 0.2
    percentual_ir = '20%'

print(f'\nSalario Bruto: R$ {salario_bruto}')
print(f'(-) IR ({percentual_ir}): R$ {imposto_de_renda}')
print(f'(-) INSS (10%): R$ {salario_bruto * 0.1}')
print(f'FGTS (11%): R$ {salario_bruto * 0.11}')
total_descontos = imposto_de_renda + (salario_bruto * 0.1)
print(f'Total de descontos: R$ {total_descontos}')
print(f'Salário Liquido: R$ {salario_bruto - total_descontos}')













