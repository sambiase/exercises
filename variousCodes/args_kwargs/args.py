# example usage of *args

def soma(*args):
    aux = 0
    for i in args:
        aux += i
    print(f'Soma = {aux}')
    print(f'Args is a {type(args)}')


if __name__ == '__main__':
    soma(5, 3)
