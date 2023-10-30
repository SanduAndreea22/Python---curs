print('exercitiu 1')
'''
1.Avand lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel'] 

Foloseste un for ca sa iterezi prin toata lista si sa afisezi;
?	Masina mea preferata este x.
?	Fa acelasi lucru cu un for each.
?	Fa acelasi lucru cu un while.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for car in range(len(masini)):
    print(f'Masina mea favorita este {masini}')
print('*' * 50)
for masina in masini:
    print(f'Masina mea favorita este {masini}')
print('*' * 50)
car = 0
while car < len(masini):
    print(f'Masina mea favorita este {masini[car]}')
    car += 1
print('*'*50)
print('exercitiu 2')
'''
2. Aceeasi lista:
Foloseste un for else
In for
-	Modifica elementele din lista astfel incat sa fie scrise cu majuscule, exceptand primul si ultimul.
In else:
-	  Printeaza lista.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for car in range(1, len(masini) - 1):
    masini[car] = masini[car].upper()
else:
    print(masini)

for i, masina in enumerate(masini):
    if i != 0 and i != len(masini)-1:
        masini[1]= masini[i].upper()
    else:
        print(masini)

print('*'*50)
print('exercitiu 3')
'''
3. Aceeasi lista:
Vine un cumparator care doreste sa cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasa de tine.
Daca masina e mercedes:
   Printeaza am gasit masina dorita de dvs
   Iesi din ciclu folosind un cuvant cheie care face acest lucru
Altfel:
   Printeaza Am gasit masina X. Mai cautam
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina dorita')
        break
    else:
        print(f'Am gasit {masina}, mai cautam')

print('*'*50)
print('exercitiu 4')
'''
4. Aceeasi lista;
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 

-	Daca masina e Trabant sau Lastun:
   Foloseste un cuvant cheie care sa dea skip la ce urmeaza (nu trebuie else).
-	Printeaza S-ar putea sa va placa masina x.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        continue
    print(f'S-ar putea sa va placa masina {masina} ')

print('exercitiu 5')
'''
5. Modernizeaza parcul de masini:

?	Creaza o lista goala, masini_vechi.
?	Itereaza prin masini.
?	Cand gasesti Lastun sau Trabant:
-	Salveaza aceste masini in masini_vechi.
-	Suprascrie-le cu Tesla (in lista initiala de masini).
?	Printeaza Modele vechi: x.
?	Modele noi: x.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        masini_vechi.append(masina)
        i = masini.index(masina)
        masini[i] = 'Tesla'
print(f'Masini vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

for i, masina in enumerate(masini): #folosit pt indici + valori
    if masina == 'Trabant' or masina == 'Lastun':
        masini_vechi.append(masina)
        masini[i] = 'Tesla'
print(masini)
print(masini_vechi)
print('*'*50)
print('exercitiu 6')
'''
6. Avand dict:
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

?	Prezinta doar masinile care se incadreaza in acest buget.
?	Itereaza prin dict.items() si acceseaza masina si pretul.
?	Printeaza Pentru un buget de sub 15000 euro puteti alege masina xLastun
?	Itereaza prin lista.
'''
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

buget = 15000
for masina, pret in pret_masini.items():
    if pret <buget:
        print(f'Pentru un buget sub 1500 puteti alege masina {masina}')

print('*'*50)
print('exercitiu 7')
'''
7. Avand lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
?	Itereaza prin ea.
?	Afiseaza de cate ori apare 3 (nu ai voie sa folosesti count).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

trei = 0
for numar in numere:
    if numar == 3:
        trei += 1

print(trei)

print('*'*50)
print('execitiu 8')
'''
8. Aceeasi lista:
?	Itereaza prin ea
?	Calculeaza si afiseaza suma numerelor (nu ai voie sa folosesti sum).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

suma = 0
for numar in numere:
    suma += numar
print(suma)

print('*'*50)
print('execitiu 9')
'''
9. Aceeasi lista:
?	Itereaza prin ea.
?	Afisaza cel mai mare numar (nu ai voie sa folosesti max).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim = float('-inf')
for numar in numere:
   if maxim <= numar:
       maxim = numar
print(maxim)

print('*'*50)
print('exrcitiu 10')
'''
10. Aceeasi lista:
?	Itereaza prin ea.
?	Daca numarul e pozitiv, inlocuieste-l cu valoarea lui negativa.
Ex: daca e 3, sa devina -3
?	Afisaza noua lista.
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

print('exercitiu 11')
'''
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin lista alte_numere 
Populeaza corect celelalte liste
Afiseaza cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar %2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

print('exercitiu 12')
'''
12. Aceeasi lista:
Ordoneaza crescator lista fara sa folosesti sort.
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
lenght = len(alte_numere)

sort = False
while not sort:
    sort = True
    for i in range(lenght - 1):
        if alte_numere[i] > alte_numere[i + 1]:
            temp = alte_numere[i]
            alte_numere[i] = alte_numere[i+ 1]
            alte_numere[i+ 1] = temp
            sort = False
print(alte_numere)
print('*'*80)
n = 0
alte_numere_sortate = []
while len(alte_numere) >0:
    alte_numere_sortate.append(min(alte_numere))
    alte_numere.remove(min(alte_numere))
    n += 1
print(alte_numere_sortate)
