'''
   Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

        quantos espaços em branco existem na frase.
        quantas vezes aparecem as vogais a, e, i, o, u.

'''

frase = 'Eu sou mengao'

vogal_a = frase.count('a')
vogal_e = frase.count('e')
vogal_i = frase.count('i')
vogal_o = frase.count('o')
vogal_u = frase.count('u')
esp_em_branco = frase.count(' ')

print(f'Vogal a --> {vogal_a}')
print(f'Vogal e --> {vogal_e}')
print(f'Vogal i --> {vogal_i}')
print(f'Vogal o --> {vogal_o}')
print(f'Vogal u --> {vogal_u}')
print(f'Espaços em Branco --> {frase.count(" ")}')