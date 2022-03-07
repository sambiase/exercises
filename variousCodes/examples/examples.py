import string

pwd = 'password12'
capitalList = []
numList = []
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
punctList = []

for i in punctuations:
    punctList.append(i)

if (7 < len(pwd) <= 31) and ('password' not in pwd.upper() and 'password' not in pwd.lower()):
    capitalList = [str(capital) for capital in pwd.strip() if 'A' <= capital <= 'Z']
    numList = [int(numbers) for numbers in pwd.strip() if numbers.isdigit()]




print(f'Capital Letters: {capitalList}')
print(f'Numbers: {numList}')






