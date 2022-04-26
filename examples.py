

def to_upper(func):
    def wrapper():
        nome = func()
        print(nome.upper())
    return wrapper

@to_upper
def print_nome():
    return 'flamengo'

print_nome()

