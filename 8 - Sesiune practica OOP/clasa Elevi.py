from abc import ABC, abstractmethod

class Elevi():
    nume = None
    varsta = None
    buline_rosii = 0

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta
class Gradinita(ABC):

    @abstractmethod
    def activiate_practica(self):
        raise NotImplementedError

    @abstractmethod
    def ore_somn(self):
        pass


class GradinitaPublica(Gradinita):

    def activiate_practica(self):
        print('copiii invata sa deseneze')

    def ore_somn(self):
        print('copiii dorm')

class GradinitaPrivata(Gradinita):

    def activiate_practica(self):
        print('copiii invata sa modele cu plastiloina')

    def ore_somn(self):
        pass


class GradinitaPublica25(GradinitaPublica):
    elevi = []
    __arie = 0
    _intrari = 0
    adresa = None


    def __init__(self, elevi, arie, adresa, intrari):
        self._intrari = intrari
        self.elevi = elevi
        self.__arie = arie
        self.adresa = adresa

    @property
    def arie(self):
        return self.__arie

    @arie.getter
    def arie(self):
        return self.__arie

    @arie.setter
    def arie(self, value):
        self.__arie = value

    @arie.deleter
    def arie(self):
        self.__arie = None


    '''def get_buline_rosii(self):
        suma_buline = 0
        for i, elev in enumerate(self.elevi):
            buline_rosii_actuale = int(input(f'dati un nr de buline rosii pentru {elev.nume}'))
            self.elevi[i].buline_rosii = buline_rosii_actuale
            suma_buline += buline_rosii_actuale

        media_buline = suma_buline / len(self.elevi)
        if media_buline > 5:
            print('elevi neastamparati') '''


elev_1 = Elevi('George', 12 )
elev_2 = Elevi('Ame', 9)
elev_3 = Elevi('Deea', 11)

elevi = [elev_1, elev_2, elev_3]

gradinita_publica25 = GradinitaPublica25(elevi, 157, 'Pipera', 4)
print(gradinita_publica25.arie)
gradinita_publica25.arie = 184
print(gradinita_publica25.arie)
del gradinita_publica25.arie
print(gradinita_publica25.arie)





















