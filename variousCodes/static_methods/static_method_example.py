'''

    Static Methods are methods that does not need parameters to be passed to the method
    In Python we use: @staticmethod notation above the method
'''


class Carro:
    def __init__(self):
        pass


    @staticmethod
    def print_carro():
        return f'Fiat'


carro = Carro()
print(carro.print_carro())