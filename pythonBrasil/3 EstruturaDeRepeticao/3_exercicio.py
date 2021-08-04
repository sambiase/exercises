'''
    Faça um programa que leia e valide as seguintes informações:
        Nome: maior que 3 caracteres;
        Idade: entre 0 e 150;
        Salário: maior que zero;
        Sexo: 'f' ou 'm';
        Estado Civil: 's', 'c', 'v', 'd';
'''

aux = 0
while aux == 0:
    nome = str(input('Nome --> '))
    if len(nome) > 3:
        idade = int(input('Idade --> '))
        if 0 < idade < 150:
            salario = float(input('Salario --> '))
            if salario > 0:
                sexo = str(input('Sexo (M) ou (F) --> '))
                if sexo.upper() == 'M' or sexo.upper() == 'F':
                    estado_civil = str(input('Estado Civil - (S) (C) (V) (D) --> '))
                    estado_civil_lista = ['s','c','v','d']
                    if estado_civil in estado_civil_lista:
                        print('Todos os Dados OK')
                        aux = 1

    else:
        print('Info incorreta.')






