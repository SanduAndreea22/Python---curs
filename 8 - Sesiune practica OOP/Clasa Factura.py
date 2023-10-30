from datetime import date


class Factura:
    seria = 'XYZ'
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, nume_produs, cantitate, pret_buc):
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
        self.today = date.today()

    def schimba_cantitatea(self, noua_cantitate):
        self.cantitate = noua_cantitate

    def schimba_pret(self, noul_pret):
        self.pret_buc = noul_pret

    def schimba_nume_produs(self, noul_nume_produs):
        self.nume_produs = noul_nume_produs

    def genereaza_factura(self):
        pret_total = self.cantitate * self.pret_buc
        print(f"Produs: {self.nume_produs}, Cantitate: {self.cantitate}, Pret buc: {self.pret_buc}, Pret total: {pret_total}, Data: {self.today}")

telefon = Factura("telefon", 3, 1200)
laptop = Factura("laptop", 2, 2500)
telefon.genereaza_factura()
print(telefon)
print(laptop)
print("_" * 100)
telefon.schimba_cantitatea(5)
telefon.schimba_nume_produs('telefon mobil')
telefon.schimba_pret(900)
telefon.genereaza_factura()
print("_" * 100)
telefon.schimba_cantitatea(5)
telefon.schimba_nume_produs('telefon mobil')
telefon.schimba_pret(900)
telefon.genereaza_factura()
print("_" * 100)
laptop.genereaza_factura()
print("_" * 100)
laptop.genereaza_factura()
print("_" * 100)
laptop.genereaza_factura()
print("_" * 100)
laptop.genereaza_factura()
