'''
   Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
   encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
   Após esta entrada de dados, faça:

        Mostre a quantidade de valores que foram lidos;
        Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
        Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
        Calcule e mostre a soma dos valores;
        Calcule e mostre a média dos valores;
        Calcule e mostre a quantidade de valores acima da média calculada;
        Calcule e mostre a quantidade de valores abaixo de sete;
        Encerre o programa com uma mensagem;
'''

lista_de_notas = []
while True:
    nota = float(input('Digite uma nota --> '))
    if nota >= 0:
        lista_de_notas.append(nota)
    else:
        break

print(f'\nQuantidade de valores lidos --> {len(lista_de_notas)}')
print(' '.join([str(nota) for nota in lista_de_notas]))
lista_de_notas.reverse()

for _,v in enumerate(lista_de_notas):
    print(f'Todos os valores informados em ordem inversa --> {v}')

soma = sum(lista_de_notas)
print(f'Soma dos valores --> {sum(lista_de_notas)}')
media = soma / len(lista_de_notas)
print(f'Media dos valores --> {round(media,2)}')

print(f'Quantidade de Valores acima da Media --> {[str(nota) for nota in lista_de_notas if nota > media]}')

print(f'Quantidade de Valores abaixo de Sete --> {[str(nota) for nota in lista_de_notas if nota < 7]}')
print(f'\n##############Programa Encerrado')

