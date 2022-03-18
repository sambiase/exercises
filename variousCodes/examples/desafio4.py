# password checker


import string as punc
booleano = False

pwd = 'adasd2344$$'

if len(pwd) < 7 or len(pwd) >= 31:
    print('Password must be longer than 7 and shorter than 31 chars')

elif 'password' in pwd.upper() or 'password' in pwd.lower():
    print('Name "password" cannot be part of the string')

elif not [str(capital) for capital in pwd.strip() if 'A' <= capital <= 'Z']:
    print('Password must contain a capital letter')

elif not [int(numbers) for numbers in pwd.strip() if numbers.isdigit()]:
    print('Password must at least contain one number')

elif not [bool(i) for i in pwd if i in punc.punctuation]:
    print('Password must contain a punctuation mark or math symbol')

else:
    print(f'Password accepted :)')
    booleano = True







