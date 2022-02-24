# funcao que calcula a soma de dois numeros e trata excecoes

def div(n1,n2):
    try:
        res = n1 / n2
    except ZeroDivisionError:
        print('Divisao por zero nao pode')
    else:
        print(f'Res da Divisao: {res}')
    finally:
        print('Finally executada')


if __name__ == '__main__':
    div(4,0)
