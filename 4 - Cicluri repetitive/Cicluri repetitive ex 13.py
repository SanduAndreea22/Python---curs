print('exercitiu 13')
'''
13. Ghicitoare de numar:
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
?	Nr secret e mai mare
?	Nr secret e mai mic
?	Felicitari! Ai ghicit!
'''
import random

numar_secret = random.randint(1,30)
numar_ghicit = None

while numar_ghicit != numar_secret:
    numar_ghicit = int(input('alege un numar intre 1 si 30: '))
    if numar_ghicit == numar_secret:
        print('Felicitari, ai ghicit')
    elif numar_ghicit < numar_secret:
        print('Nr secret e mai mare')
else:
    print('Nr secret e mai mic')



