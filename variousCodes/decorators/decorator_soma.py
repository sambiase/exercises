
def soma (func):
    def wrapper():
        nums= func()
        aux = 0
        for i in nums:
            aux += i
        print(f'Soma dos numeros: {aux}')
    return wrapper


@soma
def nums ():
    numsLista = [1 ,2 ,3]
    return numsLista


nums()
