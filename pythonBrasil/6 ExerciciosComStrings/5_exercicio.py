'''
   Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

        FULANO
        FULAN
        FULA
        FUL
        FU
        F
'''

nome = 'fulano'
aux = len(nome)

for i in nome:
    print(nome[:aux].upper())
    aux -= 1