import random

esco=int(input('digite um numero entra 0 a 5: '))
numero=[1,2,3,4,5]
bot=random.choice(numero)

if esco==bot:
    print('cara bom')
else:
    print('cara ruim')

