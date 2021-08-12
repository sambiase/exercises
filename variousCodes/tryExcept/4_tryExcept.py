'''
    try except com isinstance
'''

num = 1.1
res = isinstance(num,str)
try:
    res
except TypeError:
    print('ERRO')

