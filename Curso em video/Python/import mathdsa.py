import math
catetu=float(input('digite o cateto da oposto: '))
cateto2=float(input('digite o cateto da adjaceste: '))
hipo=math.hypot(catetu,cateto2)
print('a hipotenusa é {:.3}'.format(hipo))