'''
    Sort de uma lista de ints
'''

lista = [3, 4, 50, 2, 1, 10, 34]

for i in range(len(lista)):
    for v in range(i + 1, len(lista)):
        if lista[i] > lista[v]:
            tmp = lista[v]
            lista[v] = lista[i]
            lista[i] = tmp

print(f'Lista Ordenada: {lista}')
