'''
  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string
  no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''


def data_por_extenso(dia, mes, ano):
    mesPorExtenso = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho',
                     8: 'Agosto',
                     9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

    if dia <= 0 or dia > 31:
        return f'Dia Inexistente'
    elif mesPorExtenso.get(mes) is None:
        return f'Mes Inexistente'
    elif ano <= 1900 or ano > 2021:
        return f'Ano Inexistente'
    else:
        return f'\n{dia} de {mesPorExtenso.get(mes)} de {ano}'


if __name__ == '__main__':
    dia = int(input('Digite um dia --> '))
    mes = int(input('Digite um mes --> '))
    ano = int(input('Digite um ano --> '))
    print(data_por_extenso(dia, mes, ano))
