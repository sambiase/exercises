'''
    Um posto está vendendo combustíveis com a seguinte tabela de descontos:

        Álcool:
            até 20 litros, desconto de 3% por litro
            acima de 20 litros, desconto de 5% por litro

        Gasolina:
            até 20 litros, desconto de 4% por litro
            acima de 20 litros, desconto de 6% por litro

    Escreva um algoritmo que leia o número de litros vendidos, o tipo de
    combustível (codificado da seguinte forma: A-álcool, G-gasolina),
    calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
    gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
class Alcool:

    def __init__(self, qtd_litros_vendido):
        self.qtd_litros_vendido = qtd_litros_vendido

    def calculo_alcool(self):
        print('\nTipo de Combustivel: Alcool')
        print('Preco do litro: R$ 1,90')

        if self.qtd_litros_vendido <= 20:
            desconto = self.qtd_litros_vendido * 0.03
            valor_a_ser_pago = (self.qtd_litros_vendido * 1.9) * (1 - desconto)
            print(f'Valor a ser pago: R$ {round(valor_a_ser_pago,2)}')
        else:
            desconto = self.qtd_litros_vendido * 0.05
            valor_a_ser_pago = (self.qtd_litros_vendido * 1.9) * (1 - desconto)
            print(f'Valor a ser pago: R$ {round(valor_a_ser_pago,2)}')


class Gasolina:

    def __init__(self, qtd_litros_vendido):
        self.qtd_litros_vendido = qtd_litros_vendido

    def calculo_gasolina(self):
        print('\nTipo de Combustivel: Gasolina')
        print('Preco do litro: R$ 2,50')

        if self.qtd_litros_vendido <= 20:
            desconto = self.qtd_litros_vendido * 0.04
            valor_a_ser_pago = (self.qtd_litros_vendido * 2.5) * desconto
            print(f'Valor a ser pago: R$ {round(valor_a_ser_pago,2)}')
        else:
            desconto = self.qtd_litros_vendido * 0.06
            valor_a_ser_pago = (self.qtd_litros_vendido * 2.5) * desconto
            print(f'Valor a ser pago: R$ {round(valor_a_ser_pago,2)}')

class Combustivel:

    tipo_de_combustivel = str(input('Tipo de Combustivel: (A) - Alcool , (G) - Gasolina\t'))

    def __init__(self):
        pass

    if tipo_de_combustivel.upper() == 'A' or tipo_de_combustivel.upper() == 'G':
        qtd_litros_vendido = float(input('Quantidade de Litros vendido: '))

        if tipo_de_combustivel.upper() == 'A':
            combustivel = Alcool(qtd_litros_vendido)
            combustivel.calculo_alcool()

        elif tipo_de_combustivel.upper() == 'G':
            combustivel = Gasolina(qtd_litros_vendido)
            combustivel.calculo_gasolina()

    else:
        print('Opcao Invalida')



