lista = [50,10,2,-10]

for i in range(len(lista)):
    for n in range(i+1,len(lista)):
        if lista[i] > lista [n]:
            tmp = lista [n]
            lista[n] = lista[i]
            lista[i] = tmp

print(f'Lista Ordenada: {lista}')