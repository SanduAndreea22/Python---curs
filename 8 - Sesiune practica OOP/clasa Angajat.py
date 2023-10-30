class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(f'Angajata {self.nume} {self.prenume} are salariul de {self.salariu} ')

    def nume_complet(self):
        print(f'Angajatul se numeste {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar al angajatului este {self.salariu}')

    def salariu_anual(self):
        print(f'Salariul anual al angajatului este {12*self.salariu}')

    def marire_salariu(self, procent):
        self.salariu += (self.salariu * procent) / 100
        print(f'Angajatul {self.nume} {self.prenume} a primit o marire de {procent}. Noul salariu este de {self.salariu}')

angajat_1 = Angajat('A', "Cosmin", 1200)
angajat_2 = Angajat('S', 'Andreea', 3500)
angajat_3 = Angajat('G', 'Ame', 5500)
angajat_1.descriere()
angajat_2.descriere()
angajat_3.descriere()
print("_" * 100)
angajat_1.nume_complet()
angajat_2.nume_complet()
angajat_3.nume_complet()
print("_" * 100)
angajat_1.salariu_lunar()
angajat_2.salariu_lunar()
angajat_3.salariu_lunar()
print("_" * 100)
angajat_1.salariu_anual()
angajat_2.salariu_anual()
angajat_3.salariu_anual()
print("_" * 100)
angajat_1.marire_salariu(-20)
angajat_2.marire_salariu(10)
angajat_3.marire_salariu(7)
print("_" * 100)
angajat_1.descriere()
angajat_2.descriere()
angajat_3.descriere()




