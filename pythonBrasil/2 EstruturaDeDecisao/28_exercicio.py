'''
    O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                              Até 5 Kg           Acima de 5 Kg
        File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
        Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
        Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

        Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
        carne da promoção, porém não há limites para a quantidade de carne por cliente.
        Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5%
        sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
        comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
        tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

tipo_de_carne = int(input('Digite o tipo de Carne: 1 - File Duplo, 2 - Alcatra, 3 - Picanha\t'))
lista_tipo_de_carnes = {1: 'File Duplo', 2: 'Alcatra', 3: 'Picanha'}
tipo_de_pagamento = str(input('Pagar com Cartao Tabajara? (S) ou (N)'))


if tipo_de_carne in lista_tipo_de_carnes.keys():
    qtd_de_carne = float(input('Digite a quantidade de Carne desejada: '))
    if qtd_de_carne <= 5:
        if tipo_de_carne == 1:
            preco_total = qtd_de_carne * 4.9
        elif tipo_de_carne == 2:
            preco_total = qtd_de_carne * 5.9
        else:
            preco_total = qtd_de_carne * 6.9
    else:
        if tipo_de_carne == 1:
            preco_total = qtd_de_carne * 5.8
        elif tipo_de_carne == 2:
            preco_total = qtd_de_carne * 6.8
        else:
            preco_total = qtd_de_carne * 7.8
else:
    print('Opcao Invalida')


print(f'Tipo de Carne Comprada: {lista_tipo_de_carnes.get(tipo_de_carne)}')
print(f'Quantidade de Carne Comprada: {qtd_de_carne}')
print(f'Preco Total: R$ {preco_total}')

if tipo_de_pagamento.upper() == 'S':
    print('Tipo de Pagamento: Cartao Tabajara')
    print('Valor do Desconto: 5%')
    print(f'Valor a Pagar: R$ {preco_total * 0.95}')
elif tipo_de_pagamento.upper() == 'N':
    print('Tipo de Pagamento: Outros')
    print(f'Valor a Pagar: R$ {preco_total}')
else:
    print('Opcao Invalida de Pagamento')



