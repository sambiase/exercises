def to_upper(func):
    def wrapper():
        nome = func()
        print(f'Nome: {nome.upper()}')

    return wrapper


@to_upper
def cumprimento():
    return 'Ola Pessoal. Tudo bem?'


cumprimento()
