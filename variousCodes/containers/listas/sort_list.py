lista = [50, 10, 2, -10]
option = 's'
while option.upper() == 'S':

    res = int(input('Alternativa (1) ou Alternativa (2): \t'))
    if res == 1:
        for i in range(len(lista)):
            for n in range(i + 1, len(lista)):
                if lista[i] > lista[n]:
                    tmp = lista[n]
                    lista[n] = lista[i]
                    lista[i] = tmp

        print(f'Alternativa 1: {lista}')

    elif res == 2:
        for i in range(len(lista)):
            for n in range(i + 1, len(lista)):
                if lista[i] > lista[n]:
                    lista[n], lista[i] = lista[i], lista[n]

        print(f'Alternativa 2: {lista}')

    else:
        print(f'Alternativa Incorreta')

    option = str(input('Continuar? (S) (N)\t'))
