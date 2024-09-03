cont=0
muier=0
homem=0
for p in range (0,4):
    nome=input('Digite seu nome: ')
    sexo=input('Digite seu sexo com F e M: ')
    idade=int(input('Digite sua idade: '))
    cont = idade + cont
    muier = idade <=20
print('a média é {}'.format(cont/4))