def cumprimento():
    print ('Bem vindo')

def primeiro_nome (nome='Andre'):
    return nome

def segundo_nome (sobrenome='Silva'):
    cumprimento()
    print(f'Nome: {primeiro_nome()}')
    print(f'Sobrenome: {sobrenome}')

segundo_nome()