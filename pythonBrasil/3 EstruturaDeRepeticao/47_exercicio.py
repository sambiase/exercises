'''
    Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
    A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
    Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
    alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a
    descrição acima informada (retirar o melhor e o pior salto e depois calcular a média
    com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída
    do programa deve ser conforme o exemplo abaixo:

        Atleta: Aparecido Parente
        Nota: 9.9
        Nota: 7.5
        Nota: 9.5
        Nota: 8.5
        Nota: 9.0
        Nota: 8.5
        Nota: 9.7

        Resultado final:
        Atleta: Aparecido Parente
        Melhor nota: 9.9
        Pior nota: 7.5
        Média: 9,04
'''

nome_atleta = str(input('Nome do Atleta: '))
jurado_1 = float(input('Nota Jurado 1: '))
jurado_2 = float(input('Nota Jurado 2: '))
jurado_3 = float(input('Nota Jurado 3: '))
jurado_4 = float(input('Nota Jurado 4: '))
jurado_5 = float(input('Nota Jurado 5: '))
jurado_6 = float(input('Nota Jurado 6: '))
jurado_7 = float(input('Nota Jurado 7: '))

lista_notas = [jurado_1, jurado_2, jurado_3, jurado_4, jurado_5, jurado_6, jurado_7]
lista_notas.sort()
pior_nota = lista_notas[0]
melhor_nota = lista_notas[6]
notas_total = 0

print(f'Nome: {nome_atleta}')
for notas in lista_notas:
    print(f'Nota: {notas}')

print(f'\nResultado Final:')
print(f'Atleta: {nome_atleta}')
print(f'Melhor Nota: {melhor_nota}')
print(f'Pior Nota: {pior_nota}')
lista_notas.pop(0)
lista_notas.pop(6)
for i in lista_notas:
    notas_total += i

print(f'Media: {notas_total/5}')
