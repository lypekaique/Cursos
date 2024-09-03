soma=0
cont=0
for n in range (0,6):
    a=int(input('digite um numero:'))
    if a % 2 == 0:
     soma += a
     cont += 1
    
print(' os pares são {} a soma é igual a {}'.format(cont,soma))