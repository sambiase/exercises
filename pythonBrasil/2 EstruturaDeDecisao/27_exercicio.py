'''
    Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                              Até 5 Kg           Acima de 5 Kg
        Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
        Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
    ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
    adquiridas e escreva o valor a ser pago pelo cliente.
'''

qtd_morangos = float(input('Quantidade de Morangos comprados (kg): '))
qtd_macas = float(input('Quantidade de Macas compradas (kg): '))


def calcular_valor_morango(qtd_morangos):
    if qtd_morangos <= 5:
        valor_morango = qtd_morangos * 2.5
    else:
        valor_morango = qtd_morangos * 2.2

    return valor_morango

def calcular_valor_maca(qtd_macas):
    if qtd_macas <= 5:
        valor_maca = qtd_macas * 1.8
    else:
        valor_maca = qtd_macas * 1.5

    return valor_maca

if (qtd_morangos + qtd_macas) > 8 or (calcular_valor_morango(qtd_morangos) + calcular_valor_maca(qtd_macas)) > 25:
    valor_com_desconto = (calcular_valor_morango(qtd_morangos) + calcular_valor_maca(qtd_macas)) * 0.9
    print(f'Valor a ser pago com Desconto de 10%: R$ {valor_com_desconto}')
else:
    print(f'Valor a ser pago sem Desconto: R$ {calcular_valor_morango(qtd_morangos)+calcular_valor_maca(qtd_macas)}')