import random
n0=input('digite o primeiro nome: ')
n1=input('digite o segundo nome: ')
n2=input('digite o terceiro nome: ')
n3=input('digite o quarto nome: ')

pessoas=[n0, n2, n3, n3]

sor=random.choice(pessoas)

print('o sortudo foi {}'.format(sor))



