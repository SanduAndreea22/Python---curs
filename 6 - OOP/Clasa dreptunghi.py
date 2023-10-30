'''
2. Clasa Dreptunghi
     Atribute: lungime, latime, culoare
     Constructor pentru toate atributele
     Metode:
?	descrie()
?	aria()
?	perimetrul()
?	schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si parametru o noua culoare si va suprascrie atributul self.culoare. Poti verifica schimbarea culorii prin apelarea metodei descrie().

'''
import math
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f'Dreptunghiul are culoarea {self.culoare}, o lungime de {self.lungime} cm si o latime de {self.latime} cm')

    def aria(self):
        return self.lungime * self.lungime
    def perimetru(self):
        return self.lungime * self.latime
    def schimba_culoarea(self, culoare_noua):
        self.culoare_noua = culoare_noua

drept1 = Dreptunghi(12, 3, 'albastru')
print(drept1.descriere())
print(drept1.aria())
print(drept1.perimetru())
print(drept1.schimba_culoarea('verde'))


