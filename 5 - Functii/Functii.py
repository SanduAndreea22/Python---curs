import math
print(math.cos(3))
print(math.sqrt(3))

print('exercitiu 1')
'''
1. Scrieti o functie care primeste ca parametru lungimea laturii unui patrat si returneaza aria sa.
'''
def aria(lungime):
    arie_patrat = 4*lungime
    return arie_patrat
print(aria(6))

print('exercitiu 2')
'''
2. Scrieti un subprogram care primeste ca parametru lungimea laturii unui patrat si returneaza atat lungimea diagonalei, cat si perimetrul patratului.
'''
def arie_diagionala(lungime):
    arie_patrat = 4*lungime
    diagonala = lungime * math.sqrt(2)
    return arie_patrat,diagonala

print(arie_diagionala(2))

print('exrcitiu 3')
'''
3. Scrieti o functie care primeste ca parametri de intrare lungimile celor doua catete ale unui triunghi dreptunghic si returneaza lungimea ipotenuzei.
'''
def lengh_hyp(cat1, cat2):
    result = math.sqrt(cat1**2 + cat2**2)
    return result
print(lengh_hyp(3,7))

print('exercitiu 4')
'''
4. Scrieti o functie care primeste 3 parametri de tip real, cu semnificatia de lungimi pentru 3 segmente. Functia va returna 1 daca cele trei segmente pot forma un triunghi si 0, in caz contrar.
'''
def triungle(a,b,c):
    if a + b > c and a + c >b and b+c > a:
        return True
    else:
        return False

print(triungle(4,2,9))

print('exercitiul 1')
'''
1.Functie care sa calculeze si sa returneze suma a doua numere
'''
def sum (a, b):
    return a + b

print(sum(7,9))

print('exercitiul 2')
'''
2. Functie care sa returneze TRUE daca un numar este par, FALSE pentru impar
'''
def is_old (number):
    if number % 2:
        return True
    else:
        return False

print(is_old(3))

print('exercitii 3')
'''
3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
'''
def total_cher(name, surname, middle_name =''):
    return len(name+surname+middle_name)

print(total_cher('Sandu', 'Luiza', 'Andreea'))

print('exercitiu 4')
'''
4. Functie care returneaza aria dreptunghiului
'''
def aria_dreptunghiului(lungime, latime):
    return int(lungime) + int (latime)

print(aria_dreptunghiului(7,9))

print('exercitiu 5')
'''
5. Functie care returneaza aria cercului
'''
def aria_cerc(raza):
    return 3,14*raza*raza

print(aria_cerc(7))

print('exercitiu 6')
'''
6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat si False daca nu gaseste.
'''
def string_includes(string:str, x:str):
    if len(x) != 1:
        raise Exception('Incorrect input')
    return x in string

try:
    print(string_includes('ana are mere', 'a'))
except Exception as ex:
    print(ex.args[0])

print('exercitiu 7')
'''
7. Functie fara return, primeste un string si printeaza pe ecran:
?	Numarul de caractere lower case este x
?	Numarul de caractere upper case exte y 
'''
def count_lower_upper(string:str):
    count_lower = 0
    count_upper = 0
    for char in string:
        if char.isalpha():
            if char.islower():
                count_lower += 1
            else:
                count_upper += 1

    print(count_lower)
    print(count_upper)

count_lower_upper('Ana are merE')

print('exercitiu 8')
'''
8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive.
'''
def positive_number(numbers):
    positive_list = []
    for number in numbers:
        if number > 0:
            positive_list.append(number)
    print(f'Numere pozitive sunt {positive_list}')

positive_number([5, 21, -4, -77, -0.25, 3.14])

print('exercitiu 9')
'''
9. Functie care nu returneaza nimic. Primeste doua numere si PRINTEAZA
?	Primul numar x este mai mare decat al doilea numar y
?	Al doilea numar y este mai mare decat primul numar x
?	Numerele sunt egale. 
'''
def highter_number(a,b):
    if a > b:
        print(f'{a} este mai mare decat {b} ')
    elif a < b:
        print(f'{a} este mai mic decat {b}')
    else:
        print(f'{a} este egal cu {b}')

highter_number(7,9)

print('exercitiu 10')
'''
10. Functie care primeste un numar si un set de numere.
?	Printeaza am adaugat numarul nou in set + returneaza True
?	Printeaza nu am adaugat numarul in set. Acesta exista deja + returneaza False
'''
def set_number(number, set):
    if number in set:
        print('Nu am adaugat numarul. Acesta exista deja')
        return False
    else:
        set.add(number)
        print('Am adaugat numarul in set')
        return True

number = 6.11
set = {6.11, 22, -5.4, 7.3}
set_number(number, set)

print('exercitiu 11')
'''
11. Functie care primeste o luna din an si returneaza cate zile are acea luna.
'''
months = {
    'Jan' : 31,
    'Feb' : 28,
    'Mar' : 31,
    'Apr' : 30,
    'May' : 31,
    'Jun' : 30,
    'Jul' : 31,
    'Aug' : 31,
    'Sept' : 30,
    'Oct' : 31,
    'Nov' : 30,
    'Dec' : 31}

def day_month(month):
    return months[month]

print(day_month('Oct'))

print('exercitiul 12')
'''
12. Functie calculator care sa returneze 4 valori. Suma, diferenta, inmultirea, impartirea a doua numere.

In final vei putea face:
a, b, c, d = calculator(10, 2)
?	print("Suma: ", a)
?	print("Diferenta: ", b)
?	print("Inmultirea: ", c)
?	print("Impartirea: ", d)
'''
def calculator(a, b):
    suma = a + b
    diferenta = a - b
    inmultirea = a * b
    impartirea = a / b
    return suma, diferenta, inmultirea, impartirea

print(calculator(5,9))

print('exercitiu 13')
'''
13. Functie care primeste o lista de cifre (adica doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
def get_digits_count(digits:list):
    digits_count = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }
    for digit in digits:
        digits_count[digit] += 1
    return digits_count

print(get_digits_count([1, 3, 1, 5, 9, 7, 7, 5, 5]))

print('exercitiu 14')
'''
14. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
'''
def max_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_number(6,3,2))

print('exercitul 15')
'''
15. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar.
Exemplu: daca dam numarul 3, suma va fi 6 (0+1+2+3)
'''
def suma_numar(number):
    suma_numar = 0
    for n in range(0, number + 1):
        suma_numar += number
    return suma_numar

print(suma_numar(8))

print('exercitiul 16')
'''
16.Functie care primeste 2 liste de numere (numerele pot fi dublate). Returnati numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
'''
def get_lists_intesection(lista_1: list, lista_2: list):
    setul_1 = set(lista_1)
    setul_2 = set(lista_2)
    setul_3 = setul_1.intersection(setul_2)
    return setul_3


print('exercitiu 17')
'''
17. Functie care sa aplice o reducere de pret.
Daca produsul costa 100 lei si aplicam reducere de 10%. Pretul va fi 90 de lei.
Trateaza cazurile in care reducerea e invalida. De exemplu o reducere de 110% e invalida.

'''
def discount(price, discount):
    if discount < 100:
        new_price = price - (discount*price/100)
        print(new_price)
    else:
        print('discount invalid')

discount(50,20)

print('exercitiul 18')
'''
 18.Functie care sa afiseze data si ora curenta din Romania.
'''
import datetime
def show_date_and_time(country):
     if country == "Romania":
         now = datetime.datetime.now()
         print("Current date and time in Romania is : ")
         print(now.strftime("%Y-%m-%d %H:%M:%S"))

print(show_date_and_time('Romania'))

print('exercitiul 19')
'''
19. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la Craciun daca nu vrei sa ne zici cand e ziua ta :)
'''
def birthday(year, month, day):
    dt = datetime.datetime
    cr_year = year
    cr_month = 12
    cr_day = 25
    if cr_year == year and month == 12 and day >= 22:
        cr_year += 1
    time_left = dt(cr_year, cr_month, cr_day) - dt(year, month, day)
    print(f"Days left until my birthday : {time_left.days}")

birthday(2023,10,30)

print('exercitiu 5')
'''
5. Scrieti o functie care returneaza prima cifra a unui numar natural. De exemplu, daca parametrul efectiv este 127, functia va returna 1.
'''
def prima_cifra(numar):
    while numar >= 10:
        numar //= 10
    return numar

numar = 9875
rezultat = prima_cifra(numar)
print("Prima cifra a numarului {} este: {}".format(numar, rezultat))

print('exercitiu 6')
'''
6. Sa se tipareasca toate numerele prime aflate intre doi intregi cititi. Programul va folosi o functie care testeaza daca un numar este prim sau nu.
'''
def este_prim(numar):
    if numar <= 1:
        return False
    if numar <= 3:
        return True
    if numar % 2 == 0 or numar % 3 == 0:
        return False
    i = 5
    while i * i <= numar:
        if numar % i == 0 or numar % (i + 2) == 0:
            return False
        i += 6
    return True

def numere_prime_intre_limita(inferior, superior):
    for num in range(inferior, superior + 1):
        if este_prim(num):
            print(num)

inferior = int(input("Introduceti limita inferioara: "))
superior = int(input("Introduceti limita superioara: "))

print("Numere prime intre {} si {}: ".format(inferior, superior))
numere_prime_intre_limita(inferior, superior)

print('exercitiu 7')
'''
7. Scrieti un program care tipareste numerele intregi gasite intre doua valori citite, numere care se divid cu suma cifrelor lor. Programul va utiliza o functie care returneaza suma cifrelor unui numar intreg primit ca parametru.
'''
def suma_cifrelor(numar):
    suma = 0
    while numar > 0:
        suma += numar % 10
        numar //= 10
    return suma

def numere_cu_suma_cifrelor(inferior, superior):
    for num in range(inferior, superior + 1):
        if num % suma_cifrelor(num) == 0:
            print(num)

inferior = int(input("Introduceti limita inferioara: "))
superior = int(input("Introduceti limita superioara: "))

print("Numere care se divid cu suma cifrelor lor intre {} si {}: ".format(inferior, superior))
numere_cu_suma_cifrelor(inferior, superior)

