class Animal:
    def __init__(self,tipo):
        self.tipo = tipo


class Cachorro(Animal):
    def __init__(self,raca):
        self.raca = raca

    def latir (self):
        print ('au au')


if __name__ == '__main__':
    animal = Cachorro('Vira Lata')
    print(f'Raca: {animal.raca}')
    animal.latir()



