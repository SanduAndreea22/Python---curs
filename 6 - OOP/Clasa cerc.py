'''
1.Clasa Cerc
    Atribute: raza, culoare
    Constructor pentru ambele atribute
    Metode:
?	descrie_cerc() - va PRINTA culoarea si raza
?	aria() - va RETURNA aria
?	diametru()
?	circumferinta()

'''
import math
class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
    def Descriere(self):
        print(f'Culoarea cercului este {self.culoare}, iar raza este {self.raza}')

    def Aria(self):
        return math.pi*(self.raza * self.raza)
    def diametru(self):
        return 2 * self.raza
    def circumferinta(self):
        return math.pi * 2 * self.raza

cerc1 = Cerc(3.1, 'albastru')
print(cerc1.Descriere())
print(cerc1.Aria())
print(cerc1.diametru())
print(cerc1.circumferinta())
