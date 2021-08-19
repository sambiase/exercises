'''
    Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
    anual de crescimento de 3% e que a população de B seja 200000 habitantes
    com uma taxa de crescimento de 1.5%.
    Faça um programa que calcule e escreva o número de anos necessários para que a
    população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

pais_a_populacao = 80000
pais_a_taxa_anual = 1.03
pais_b_populacao = 200000
pais_b_taxa_anual = 1.015

qtd_anos = 0

while pais_a_populacao < pais_b_populacao:
    print(f'Populaçoes no ano --> {qtd_anos}')
    print(f'Populaçao de A --> {pais_a_populacao}')
    print(f'Populaçao de B --> {pais_b_populacao}')

    pais_a_populacao *= pais_a_taxa_anual
    pais_b_populacao *= pais_b_taxa_anual
    qtd_anos += 1

print(qtd_anos)


