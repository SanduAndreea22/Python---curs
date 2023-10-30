'''
ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pentru latura

ENCAPSULATION
latura este proprietate privata
Implementeaza getter, setter, deleter pentru latura
Implementeaza metoda ceruta de interfata (optional, doar daca ai ales sa implementezi metoda abstracta aria)

Clasa Cerc - mosteneste FormaGeometrica
constructor pentru raza
raza este proprietate privata
Implementeaza getter, setter, deleter pentru raza
Implementeaza metoda ceruta de interfata - in calcul foloseste field PI mostenit din clasa parinte (optional, doar daca ai ales sa implementezi metoda abstracta aria)

POLYMORPHISM
Defineste o noua metoda descrie - printeaza ‘Eu nu am colturi’

Creeaza un obiect de tip Patrat si joaca-te cu metodele lui
Creeaza un obiect de tip Cerc si joaca-te cu metodele lui


'''
from abc import ABC

class FormaGeometrica(ABC):
    PI = 3.14

    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura ** 2

    def descrie(self):
        print("Sunt patrat si am colturi")

    def get_latura(self):
        print(f"Latura este de {self.__latura}")
        return self.__latura

    def set_latura(self, latura_noua):
        print("Schimbam valoarea laturei")
        self.__latura = latura_noua

    def del_latura(self):
        print("Stergem valoarea laturei cu del sau schimbam valoarea pe NONE. "
              "In cazul acesta doar modificam valoarea in 0")
        self.__latura = 0

    latura_value = property(get_latura, set_latura, del_latura)

patrat_mic = Patrat(2)
print(patrat_mic.latura_value)
patrat_mic.latura_value = 2
print(patrat_mic.latura_value)
print(patrat_mic.aria())
del patrat_mic.latura_value
print('*'*80)

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return self.__raza * self.PI

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, noua_raza):
        if noua_raza < 0:
            print("Nu se poate seta o valaoare mai mica de 0")
        else:
            self.__raza = noua_raza

    @raza.deleter
    def raza(self):
        self.__raza = 0

cerc_mediu = Cerc(3)
print(cerc_mediu.raza)
cerc_mediu.raza = 4
print(cerc_mediu.raza)
print(cerc_mediu.aria())
del cerc_mediu.raza
print(cerc_mediu.raza)
cerc_mediu.descrie()
print('*'*80)
lista_forme_geometrice = [
    Cerc(6),
    Cerc(2),
    Patrat(9),
    Patrat(4)
]

for forma in lista_forme_geometrice:
    print(f"Aria {forma.aria()}")