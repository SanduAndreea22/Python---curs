class Masina:
    culoare = 'gri'
    viteza_actuala = 0
    culori_disponibile = {'blue', 'negru', 'rosu', 'alb', 'portocalie', 'maro'}
    marca = 'Porsche'
    inmatricula = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrere(self):
        print(f'Masina aleasa este marca {self.marca}, modelul {self.model}, are culoarea {self.culoare}. Are o viteza maxima de {self.viteza_maxima} km/ora. Statul imnmatricularii este {self.inmatricula}')

    def inmatriculata(self):
        if self.inmatricula is True:
            print('Masina este deja inmatriculata')
        else:
            self.inmatricula = True

    def vopseste(self, culoare):
        if culoare.lower() in self.culori_disponibile:
            self.culoare = culoare
        else:
            print('culoare nu este disponibila')

    def accelereaza(self, viteza):
        if viteza > 0:
            if viteza > self.viteza_maxima:
                self.viteza_actuala = viteza
            else:
                self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = 0

    def franeaza(self):
        self.viteza_actuala = 0


car = Masina('panamera', 150)
car.descrere()
car.inmatriculata()
car.vopseste('rosu')
car.vopseste('magenta')
car.accelereaza(90)
print(car.viteza_actuala)
car.accelereaza(180)
print(car.viteza_actuala)






