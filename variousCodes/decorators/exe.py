def toUpper(func):
    def wrapper():
        res = func()
        print(res.upper())
    return wrapper


@toUpper
def acelerar():
    return 'Acelerando'

acelerar()