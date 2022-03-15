

def comer (func):
    def wrapper():
        print('Estou com fome')
        func()
        print('Estou satisfeito')
    return wrapper


@comer
def comida():
    print ('Pode comer')


comida()