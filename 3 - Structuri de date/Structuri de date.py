print('exercitiu 1')
'''
1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
?	Afiseaz-o.
?	Inverseaza ordinea folosind slicing si suprascrie aceasta lista.
?	Printeaza varianta actuala (inversata).
?	Pe aceasta lista aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat.
?	Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala.
'''
note_muzica = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzica)
print(note_muzica[::-1])
note_muzica.reverse()
print(note_muzica)

print('exercitiu 2')
'''
2. De cate ori apare do?
'''
print(note_muzica.count('do'))

print('exercitiu 3')
'''
3. Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua.
'''
print(tuple(note_muzica))

print('exercitiu 4')
'''
4. Declara un dictionar cu notele muzicale de mai sus. Cheia va fi nota, iar valoarea un numar care arata de cate ori apare nota in gama. Afiseaza-l.
'''
dictionar_note = {
    'do': 2,
    're': 1,
    'mi': 1,
    'fa': 1,
    'sol': 1,
    'la': 1,
    'si': 1
}
print(dictionar_note)

print('exercitiu 3')
'''
3.Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
   Gaseste 2 variante sa le unesti intr-o singura lista. 
'''
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
print(list1 + list2)
list2.extend(list1)
print(list2)

print('exercitiu 4')
'''
4.
?	Sorteaza si afiseaza lista generata la exercitiul anterior.
?	Sorteaza numarul 0 folosind o functie.
?	Afisaza iar lista.
'''
list3 = [3, 1, 0, 2, 6, 5, 4]
print(list3)
list3.sort()
print(list3)
list3.remove(0)
print(list3)

print('exercitiu 5')
'''
5. Folosind un if verifica lista generata la exercitiul 3 si afiseaza:
?	Lista este goala.
?	Lista nu este goala.
'''
if not len(list3):
    print('lista este goala')
else:
    print('lista nu este goala')

print('exercitiu 6')
'''
6. Foloseste o functie care sa stearga lista de la exercitiul 3.
'''
list3.clear()
print(list3)

print('exercitiu 7')
'''
7. Copy paste la exercitiul 5. Verifica inca o data.
Acum ar trebui sa se afiseze ca lista e goala.
'''
if len(list3) == 0:
    print('lista este goala')
else:
    print('lista nu este goala')

print('exercitiu 8')
'''
8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Foloseste o functie ca sa afisezi Elevii (cheile)
'''
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(list(dict1.keys()))

print('exercitiu 9')
'''
9. Printeaza cei 3 elevi si notele lor
Ex: Ana a luat nota {x}
Doar nota o vei lua folosindu-te de cheie
'''
elevi = list(dict1.keys())
print(f'{elevi[0]} a luat nota: {dict1[elevi[0]]}')
print(f"Gigel a luat nota: {dict1['Gigel']}")
print(f"Dorel a luat nota: {dict1['Dorel']}")

print('exercitiu 10')
'''
10. Dorel a facut contestatie si a primit 6
?	Modifica nota lui Dorel in 6
?	Printeaza nota dupa modificare
'''
dict1['Dorel'] = 6
print(dict1)

print('exrcitiu 11')
'''
11. Gigel se transfera din clasa
?	Cauta o functie care sa il stearga
?	Vine un coleg nou. Adauga Ionica, cu nota 9
?	Printeaza noii elevi
'''
print(dict1.pop('Gigel'))
dict1['Ionica'] = 9
print(dict1)

print('exercitiu 13')
'''
13.
Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
?	Adauga in zilele_sapt luni
?	Afiseaza zile_sapt
'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

print('exercitiu 14')
'''
14.Foloseste un if si verifica daca:
?	Weekend este un subset al zilelor din saptamanii.
?	Weekend nu este un subset al zilelor din saptamanii.
'''
if len(zile_sapt.intersection(weekend)) == len(weekend):
    print('Weekendul este un set al zilelor saptamanii')
else:
    print('Weekendul nu este un set al zilelor saptamanii')

if weekend.issubset(zile_sapt):
    print('Weekendul este un set al zilelor saptamanii')
else:
    print('Weekendul nu este un set al zilelor saptamanii')

print('exercitiu 15')
'''
15. Afiseaza diferentele dintre aceste 2 seturi.
'''
print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))

print('exercitiu 16')
'''
16. Afiseaza intersectia elementelor din aceste 2 seturi.
'''
print(zile_sapt.intersection(weekend))
print(weekend.intersection(zile_sapt))