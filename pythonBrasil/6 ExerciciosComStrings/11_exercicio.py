'''
    Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo
    texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

        Digite uma letra: A
        -> Você errou pela 1ª vez. Tente de novo!

        Digite uma letra: O
        A palavra é: _ _ _ _ O

        Digite uma letra: E
        A palavra é: _ E _ _ O

        Digite uma letra: S
        -> Você errou pela 2ª vez. Tente de novo!
'''

palavra = 'flamengo'.upper()
print('A palavra é: ', end='')
erros = 0

for letra in palavra:
    print(f'_ ', end='')  # pista de quantas letras a palavra possui

conjunto_das_letras_palavra = set(palavra)
conjunto_de_letras_digitadas = set()

while (not conjunto_das_letras_palavra.issubset(conjunto_de_letras_digitadas)) and erros < 7:
    print()
    letra_digitada = str(input('Digite uma letra: ')).upper()
    conjunto_de_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_das_letras_palavra:
        print('A palavra é: ', end='')
        for letra in palavra:
            if letra in conjunto_de_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print('_ ', end='')

    else:
        erros += 1
        print(f'-> Você errou pela {erros}ª vez. Tente de novo!')

    print(f'\nLetras digitadas: {conjunto_de_letras_digitadas}', end='')

if erros < 7:
    print ('\nParabéns, você ganhou!')
else:
    print ('\nVocê perdeu :(')