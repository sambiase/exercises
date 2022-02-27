class Pessoa:

    def __init__(self):
        pass

    def print_nome(self):
        print('Andre')


if __name__ == '__main__':
    pessoa1 = Pessoa()
    pessoa1.print_nome()
    print(type(pessoa1))