'''
   Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
   O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
   Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
   ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores
   receberam salários nos seguintes intervalos de valores:

        $200 - $299
        $300 - $399
        $400 - $499
        $500 - $599
        $600 - $699
        $700 - $799
        $800 - $899
        $900 - $999
        $1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

'''

lista_vendedores = []
try:
    while True:
        venda_bruta_na_semana = float(input('Venda bruta na semana --> R$ '))
        venda_com_comissao = 200 + (venda_bruta_na_semana * 0.9)
        lista_vendedores.append(venda_com_comissao)
        opcao = str(input("Adicionar mais um vendedor? (s) (n)"))
        if opcao.upper() == 'N':
            break

    print(f'Numero de vendedores no intervalo $200 - $299 --> {len([str(valor) for valor in lista_vendedores if 200 <= valor <= 299])}')
    print(f'Numero de vendedores no intervalo $300 - $399 --> {len([str(valor) for valor in lista_vendedores if 300 <= valor <= 399])}')
    print(f'Numero de vendedores no intervalo $400 - $499 --> {len([str(valor) for valor in lista_vendedores if 400 <= valor <= 499])}')
    print(f'Numero de vendedores no intervalo $500 - $599 --> {len([str(valor) for valor in lista_vendedores if 500 <= valor <= 599])}')
    print(f'Numero de vendedores no intervalo $600 - $699 --> {len([str(valor) for valor in lista_vendedores if 600 <= valor <= 699])}')
    print(f'Numero de vendedores no intervalo $700 - $799 --> {len([str(valor) for valor in lista_vendedores if 700 <= valor <= 799])}')
    print(f'Numero de vendedores no intervalo $800 - $899 --> {len([str(valor) for valor in lista_vendedores if 800 <= valor <= 899])}')
    print(f'Numero de vendedores no intervalo $900 - $999 --> {len([str(valor) for valor in lista_vendedores if 900 <= valor <= 999])}')
    print(f'Numero de vendedores no intervalo $1000 em diante --> {len([str(valor) for valor in lista_vendedores if valor >= 1000])}')

except Exception:
    raise ValueError('Valor incorreto')