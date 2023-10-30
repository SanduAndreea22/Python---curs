
x = (float(input('X are valoarea: ')))
y = float(input('Y are valoarea:'))
print('exercitiu 2')
'''
2. Verifica si afiseaza daca x este numar natural sau nu
'''
if x==int(x) and x>0:
    print('X este numar natural')
else:
    print('X nu este numar natural')

print('exercitiu 3')
'''
3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru.
'''
if x >0:
    print('X este numar pozitiv')
elif x == 0:
    print('X este un numar neutru')
else:
    print('X este numar negativ')

print('exercitiu 4')
'''
4. Verifica si afiseaza daca x este intre -2 si 13.
'''
if x > -2 and x < 13:
    print('True')
else:
    print('false')

print('exercitiu 5')
'''
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5.
'''
if x-y < 5:
    print('true')
else:
    print('false')

print('exercitiu 6')
'''
6. Verifica daca x NU este intre 5 si 27  - a se folosi not.
'''
if x >5 and x<27:
    print('TRUE')
else:
    print('FALSE')

print('exercitiul 7')
'''
7.
x si y (int)
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare.
'''
if x == y:
    print('true')
elif x > y:
    print('x')
else:
    print('y')

print('exercitiu 8')
'''
8. 
X, y, z - laturile unui triunghi.
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
'''
x = int(input('X are valoarea:'))
y = int(input('Y are valoarea:'))
z = int(input('Z are valoarea:'))
if x == y == z:
    print('triunghiul este echilateral')
elif x == y or x == z or y ==z:
    print('triunghiul este isoscel')
else:
    print('triunghiul este oarecare')

print('exerciu 9')
'''
9. Citeste o litera de la tastatura.
    Verifica si afiseaza daca este vocala sau nu.
'''
litera = str(input('Alege o litera din alfabet:'))
vocale = 'aeiou'
if litera in vocale:
    print('litera este vocala')
else:
    print('litera este consoana')

print('exerciu 10')
'''
10.Transforma si printeaza notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
note = float(input('Alege o nota:'))
if note > 9 and note <= 10:
    print('A')
elif note > 8:
    print('B')
elif note > 7:
    print('C')
elif note > 6:
    print('D')
elif note >4:
    print('E')
elif note <= 4:
    print('F')
else:
    print('nota invalida')

print('exerciu 11')
'''
11.Verifica daca x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
x = int(input('alege un numar:'))
x_str = str(x)
if len(x_str) >= 4:
    print('x are 4 cifre')
else:
    print('x nu are 4 cifre')

if x >= 1000:
    print('x are 4 cifre')
else:
    print('x nu are 4 cifre')

print('exercitiu 12')
'''
12.Verifica daca x are exact 6 cifre.
'''
if x >= 100000:
    print('x are 6 cifre')
else:
    print('x nu are 6 cifre')

print('exercitiu 13')
'''
13.Verifica daca x este numar par sau impar (x e int).
'''
if x % 2 == 0:
    print('par')
else:
    print('impar')

print('exercitiu 14')
'''
14.      x, y, z (int)
Afiseaza care este cel mai mare dintre ele?
'''
x = int(input('X are valoarea:'))
y = int(input('Y are valoarea:'))
z = int(input('Z are valoarea:'))
if x == y == z:
    print('true')
elif x > y and x >z:
    print('x')
elif y > z and y >x:
    print('y')
else:
    print('z')

print('execitiu 15')
'''
15. 
X, y, z - reprezinta unghiurile unui triunghi
Verifica si afiseaza daca triunghiul este valid sau nu.
'''
x = int(input('Unghiul x are valoarea:'))
y = int(input('Unghiul y are valoarea:'))
z = int(input('Unghiul z are valoarea:'))
if x + y + z == 360:
    print('Triunghiul este valid')
else:
    print('triunghiul nu este valid')

print('exercitiu 16')
'''
16. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
?	Citeste de la tastatura un int x
?	Afiseaza stringul fara ultimele x caractere
Exemplu: daca ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('alege un numar:'))
string_cutter = string[0:-x]
string_cutter_v2 = string[0:x+1]
string_cutter_v3 = string[0:len(string)-x]
print(string_cutter)
print(string_cutter_v2)
print(string_cutter_v3)

print('exercitiu 17')
'''
17. Acelasi string. Declara un string nou care sa fie format din primele 5 caractere + ultimele 5.
'''
string_cut2 = string[0:x] + string[-x:]
print(string_cut2)

print('exercitiu 18')
'''
18. Acelasi string. 
?	Salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock (hint: este o functie care te ajuta sa faci asta)
?	Folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
?	output: 'Coral is either the stupidest animal or the smartest' 
'''
index_rock = string.index('rock')
print(index_rock)
print(string[:index_rock])

print('exercitiu 19')
'''
19. Joc ghicit zarul
Cauta pe net si vezi cum se genereaza un numar random
Ne imaginam ca dai cu zarul si salvam acest numar in dice_roll
Ia numarul ghicit de la utilizator
Verifica si afiseaza daca utilizatorul a ghicit
Vei avea 3 optiuni
?	Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
?	Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
?	Ai ghicit. Felicitari! Ai ales x si zarul a fost y.
'''
import random
dice_roll = random.randint(1, 6)
dice = int(input('dati un numar de zar:'))

if dice > 0 and dice <=6:
    print('felicitari, ai intrdus un nr valid')
    if (dice < dice_roll):
        print(f'ai pierdut, ai ales {dice}, dar a fost {dice_roll}')
    elif dice > dice_roll:
        print(f'ai pierdut, ai ales {dice}, dar a fost {dice_roll}')
    else:
        print('felicitari')
else:
    print('introdu un numar intre 1 si 6')

print('exercitiu 20')
'''
20.  Citeste de la tastatura un string
Verifica daca primul si ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se doreste ca programul sa fie case insensitive - 'apA' e acceptat
'''
string = input('dati un string:')
first_char = string[0].upper()
last_char = string[-1].upper()
assert first_char == last_char
print('a mers')

print('exercitiu 21')
'''
21. Avand stringul '0123456789'
?	Afiseaza doar numerele pare 
?	Afiseaza doar numerele impare
(hint: foloseste slicing, controleaza din pas)
'''
string = '0123456789'
# numere pare
print(string[0:len(string):2])
# numere impare
print(string[1::2])