'''

    Programa que Lê e imprime na tela o conteudo de um arquivo

'''

with open('times.txt','r') as arquivo:
    print(arquivo.read())