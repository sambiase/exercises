'''
    As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
    e lhe contraram para desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
    baseado no salário atual:
        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
            o salário antes do reajuste;
            o percentual de aumento aplicado;
            o valor do aumento;
            o novo salário, após o aumento.
'''

salario_colaborador_antes_do_reajuste = float(input('Informe o salario do Colaborador: R$ '))

if salario_colaborador_antes_do_reajuste <= 280:
    salario_colaborador_depois_do_reajuste = salario_colaborador_antes_do_reajuste * 1.2
    percentual_aplicado = 20
elif salario_colaborador_antes_do_reajuste > 280 and salario_colaborador_antes_do_reajuste <= 700:
    salario_colaborador_depois_do_reajuste = salario_colaborador_antes_do_reajuste * 1.15
    percentual_aplicado = 15
elif salario_colaborador_antes_do_reajuste > 700 and salario_colaborador_antes_do_reajuste <= 1500:
    salario_colaborador_depois_do_reajuste = salario_colaborador_antes_do_reajuste * 1.1
    percentual_aplicado = 10
else:
    salario_colaborador_depois_do_reajuste = salario_colaborador_antes_do_reajuste * 1.05
    percentual_aplicado = 5

print(f'\nSalario antes do reajuste: R$ {salario_colaborador_antes_do_reajuste}')
print(f'Percentual de aumento aplicado: {percentual_aplicado}%')
print(f'Valor do aumento: R$ {salario_colaborador_antes_do_reajuste * (percentual_aplicado / 100)}')
print(f'Novo Salario: R$ {salario_colaborador_depois_do_reajuste}')





