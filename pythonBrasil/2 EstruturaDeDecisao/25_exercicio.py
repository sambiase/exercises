'''
    Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

        "Telefonou para a vítima?"
        "Esteve no local do crime?"
        "Mora perto da vítima?"
        "Devia para a vítima?"
        "Já trabalhou com a vítima?"

    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
    entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

pergunta_1 = str(input('Telefonou para a vítima? (S) (N)'))
pergunta_2 = str(input('Esteve no local do crime? (S) (N)'))
pergunta_3 = str(input('Mora perto da vítima? (S) (N)'))
pergunta_4 = str(input('Devia para a vítima? (S) (N)'))
pergunta_5 = str(input('Já trabalhou com a vítima? (S) (N)'))
lista_respostas = [pergunta_1.upper(),pergunta_2.upper(),pergunta_3.upper(),pergunta_4.upper(),pergunta_5.upper()]


if lista_respostas.count('S') == 2:
    print('Classificacao: Suspeita')
elif 3 >= lista_respostas.count('S') <= 4:
    print('Classificacao: Cumplice')
elif lista_respostas.count('S') == 5:
    print('Classificacao: Assassino')
else:
    print('Classificacao: Inocente')