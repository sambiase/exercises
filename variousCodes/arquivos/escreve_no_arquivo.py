'''

    Programa escreve em um arquivo

'''

lista_times = ['Flamengo','Fluminense']
with open('times.txt','w') as arquivo:
    print(f' {arquivo.writelines(lista_times)}')