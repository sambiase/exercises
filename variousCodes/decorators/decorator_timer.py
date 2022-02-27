import time
def timer(func):
    def wrapper():
        nome = func()
        print(f'{nome.upper()}')


    return wrapper

@timer
def nome ():
    return 'Flamengo'



nome()