

lista = [5,2,4,1]


for i in range(len(lista)):
    for v in range(i+1,len(lista)):
        if lista[i] > lista[v]:
            lista[i], lista[v] = lista[v], lista[i]


print(lista)

#print(sorted(lista))