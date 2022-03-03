# filtrar numeros de uma lista que sejam maiores do que 5
res = filter(lambda num: num > 5, [2, 3, 1, 0, 5, 10, 25])
for i in res:
    print(i)
