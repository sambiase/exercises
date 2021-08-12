'''
    try except com assert
'''


try:
    assert 1 == 2
except AssertionError:
    print('1 nao é igual a 2')


# Outro exemplo usando o raise

try:
    assert 1 == 2
except AssertionError:
    raise AssertionError('Exemplo com raise')