'''
    Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
    e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de
    CDs e o valor para em cada um.
'''

qtd_cds = int(input('Quantidade de CDs --> '))
aux = 1
dic_cds = {}
valor_total_cds = 0

while aux <= qtd_cds:
    valor_cd = float(input(f'Valor do CD {aux}: R$ '))
    dic_cds[aux] = valor_cd
    aux += 1

for i in dic_cds.values():
    valor_total_cds += i

print(f'\nValor total gasto com CDs --> R$ {valor_total_cds}')
