from calendar import c
cont=0
soma=0

n=int(input('digite um numero: '))
for i in range(1, n, 2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i
print('a soma de todos {} os valores é {}'.format(cont,soma)) 
