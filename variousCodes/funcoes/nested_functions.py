# nested functions are functions within other functions

def nome(nome='Andre'):
    print(f'Nome: {nome}')

    def sobrenome(sobrenome = 'Silva'):
        print(f'Sobrenome: {sobrenome}')
        print(f'Local Variables: {locals()}')

    sobrenome()
    print(f'Local Variables: {locals()}')


nome()

