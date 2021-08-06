'''
    Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

        F
        FU
        FUL
        FULA
        FULAN
        FULANO
'''

nome = 'fulano'
aux = 1

for i in nome:
    print(nome[:aux].upper())
    aux += 1