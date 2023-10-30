print('exercitiu 14')
'''
14. Alege un numar de la tastatura
Ex: 7
Scrie un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''
nr = int(input('Alege o cifra de la 0 la 9: '))
for n in range(nr):
    for i in range(n+1):
        print(n+1, end=" ")
    print()