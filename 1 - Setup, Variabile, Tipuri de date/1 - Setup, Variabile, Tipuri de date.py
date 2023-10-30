# 1. In cadrul unui comentariu, explica cu cuvintele tale ce este o varialila.

# valiabila = cutiuta/cutiute in care punem valori
# variabila = o zona din memorie care stocheaza o valoare


# 2. Declara si initializeaza cate o variabila din fiecare tipuri de variabila.

nume = "Andreea" # string
varsta = 24 # integer
inaltime = 1.65 # float
major = True # boal

print('exercitiu 3')
# 3. Utilizeaza functia type pentru a verifica daca au tipul de date asteptat

print(type(nume))
print((type(varsta)))
print((type(inaltime)))
print((type(major)))

print('exercitiu 4')
# 4. Rotunjeste float-ul folosind functia round () si salveaza aceasta modificare in aceeasi variabila (suprascriere).
# - Verifica tipul acesteia

print(round(inaltime))

print('exercitiu 5')
# 5. Foloseste print() si printeaza in consola 4 propozitii folosind cele 4 variabile.
# Rezolva nepotrivirile de tip prin ce metoda doresti

print("numele ei este" + " " + nume)
print("varsta ei este " + str(varsta) + " "+ "ani")
print("ea are o inaltime de" + " " + str(inaltime)+" " + "m")

print('exercitiu 6')
'''
6. Citeste de la tastatura:
- numele,
- prenumele.
Afiseaza: 'Numele complet are x caractere'.
'''

nume_input = input("numele tau este: ")
prenume_input = input("prenumele tau este")
print("numele complet are : " + str(len(nume_input+prenume_input)))

print('exercitiu 7')
'''
7. Citeste de la tastatura:
- lungimea,
- latimea.
Afiseaza: 'Aria dreptunghiului este x'.
'''
lungime = input('lungimea este:')
latime = input('latimea este:')
aria = float(lungime) * float(latime)
print(f'Aria dreptunghiului este {aria}')

print('exercitiu 8/9')
'''
8. Avand stringul: 'Coral is either the stupidest animal or the smartest rock':
afiseaza de cate ori apare cuvantul 'the';
9. Acelasi string:
Afiseaza de cate ori apare cuvantul 'the';
Printeaza rezultat
'''
string ='Coral is either the stupidest animal or the smartest rock'
print(string.count('the '))

print('exercitiu 10')
'''10. Acelasi string.
Foloseste un assert ca sa verifici daca acest string contine doar numere. '''
assert 1 == 1
print(string.isdigit())

print('exercitiu 11')
'''
11. Exercitiu:
-	citeste de la tastatura un string de dimensiune impara;
-	afiseaza caracterul din mijloc.
'''
string_1 = input('Scrie un string de dimensiune impara:')
print(string_1[int(len(string_1)/2)])

print('exercitiu 12')
'''
12. Folosind o singura linie de cod :
-	citeste un string de la tastatura (ex: 'alabala portocala');
-	salveaza fiecare cuvant intr-o variabila;
-	printeaza ambele variabile pentru verificare.
'''
string_2 = input('Scrie un string:')
word1, word2 = string_2.split()
print(word1)
print(word2)

print('exercitiu 13')
'''
13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
'''
# extragem primul caracter
first_word = string_2[0]
# extragem stringul din mijloc
middle_string = string_2[1:-1]
# schimbam caracterul
middle_string = middle_string.replace(first_word, first_word.upper())
# reconstruim stringul
reconstructed_string = first_word +middle_string + string_2[-1]
print(reconstructed_string)

print('exercitiu 14')
'''
14.Exercitiu:
-	citeste un user de la tastatura;
-	citeste o parola;
-	afiseaza: 'Parola pt user x este ***** si are x caractere';
-	***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect.

eg: parola abc => ***
      parola abcd => ****
'''
user = input('dati un user name:')
password = input('dati o parola:')
password_len = len(password)
password_hashed = '*' * password_len
print(f'Parola pentru user {user} este {password_hashed} si are {password_len} caractere')