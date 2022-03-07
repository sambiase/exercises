import string as punc


def StringChallenge(strParam):

    if len(strParam) < 7 or len(strParam) >= 31:
        strParam = bool(False)

    elif 'password' in strParam.upper() or 'password' in strParam.lower():
        strParam = bool(False)

    elif not [str(capital) for capital in strParam.strip() if 'A' <= capital <= 'Z']:
        strParam = bool(False)

    elif not [int(numbers) for numbers in strParam.strip() if numbers.isdigit()]:
        strParam = bool(False)

    elif not [bool(i) for i in strParam if i in punc.punctuation]:
        strParam = bool(False)

    else:
        strParam = bool(True)

    return strParam


# keep this function call here
print(StringChallenge(input()))
