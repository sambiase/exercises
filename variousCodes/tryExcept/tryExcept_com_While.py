# try except com While

while True:
    try:
        num = int(input('Digite um Numero: '))
        break
    except ValueError:
        print('nao eh um numero. Tente novamente')


