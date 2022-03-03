
def toUpper (func):
    def wrapper():
      print(func().upper())
    return wrapper

@toUpper
def nomes ():
    return 'flamengo'


nomes()