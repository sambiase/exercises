'''
        Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

            Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
                tipoCombustivel.
                valorLitro
                quantidadeCombustivel

            Possua no mínimo esses métodos:
                abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade
                    de litros que foi colocada no veículo
                abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o
                    valor a ser pago pelo cliente.
                alterarValor( ) – altera o valor do litro do combustível.
                alterarCombustivel( ) – altera o tipo do combustível.
                alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

        OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''

class bombaCombustível:

    def __init__(self, tipoCombustivel='gasolina', valorLitro=5.25, quantidadeCombustivelNaBomba=100):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivelNaBomba = quantidadeCombustivelNaBomba

    def abastecerPorValor(self):
        valor_a_ser_abastecido = float(input('Valor a ser abastecido --> R$ '))
        qtdCombutivelColocado = valor_a_ser_abastecido / self.valorLitro
        self.quantidadeCombustivelNaBomba -= qtdCombutivelColocado
        if self.quantidadeCombustivelNaBomba < qtdCombutivelColocado:
            print('Sem combustivel suficiente na Bomba')
        else:
            self.quantidadeCombustivelNaBomba -= qtdCombutivelColocado
            return f'{qtdCombutivelColocado, valor_a_ser_abastecido}'

    def abastecerPorLitro(self):

        qtd_litros_a_ser_abastecido = float(input('Quantidade em litros a ser abastecido -->  '))
        if self.quantidadeCombustivelNaBomba < qtd_litros_a_ser_abastecido:
            print('Sem combustivel suficiente na Bomba')
        else:
            valor_a_ser_pago = qtd_litros_a_ser_abastecido * self.valorLitro
            self.quantidadeCombustivelNaBomba -= qtd_litros_a_ser_abastecido
            return valor_a_ser_pago


    def alterarValor(self):
        self.valorLitro = float(input(f'Novo valor do litro de combustivel --> R$ '))

    def alterarCombustivel(self):
        tipo_comb = str(input(('Tipo de combustivel (G)asolina - (A)lcool --> ')))
        if tipo_comb.upper() == 'G':
            print (f'Tipo de Combustivel --> Gasolina')
            self.tipoCombustivel = 'Gasolina'
        elif tipo_comb.upper() == 'A':
            print(f'Tipo de Combustivel --> Alcool')
            self.tipoCombustivel = 'Alcool'
        else:
            print ('Combustivel Inexistente')


    def adicionarQuantidadeCombustivel(self):
       pass





if __name__ == '__main__':
    bombaCombustível = bombaCombustível()
    print(f'Quantidade de litros colocados no veiculo --> {bombaCombustível.abastecerPorValor()}')
    print(f'Quantidade combustivel total na Bomba --> {bombaCombustível.quantidadeCombustivelNaBomba}')
    print(f'Valor a ser pago pelo cliente --> R$ {bombaCombustível.abastecerPorLitro()}')
    print(f'Quantidade combustivel total na Bomba --> {bombaCombustível.quantidadeCombustivelNaBomba}')
    bombaCombustível.alterarValor()
    bombaCombustível.alterarCombustivel()
    print(f'Quantidade Combustivel restante na Bomba --> {bombaCombustível.adicionarQuantidadeCombustivel()}')
