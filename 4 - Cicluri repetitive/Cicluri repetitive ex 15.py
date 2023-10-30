'''
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Itereaza prin lista 2d
Printeaza Cifra curenta este x
(hint: nested for - adica for in for)
'''
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for rand in tastatura_telefon:
    for cifra in rand:
        print(f'Cifra curenta este {cifra}')