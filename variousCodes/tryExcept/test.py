while True:
    try:
        num = int(input('Digite um numero: '))
    except ValueError:
        print('erro')
        break

