num=[]
while True:
     num.append(int(input('Digite um numero: ')))
     resp=str(input('Quer continuar ? [S/N]: '))
     
     if resp in 'Nn':
          break
print ('-=' * 30)
print(f'voce digitou {len(num)}')
num.sort(reverse=True)
print(f'valores bunitin {num}')
if 5 in num:
     print('digite tem 5 poha')
else:
     print('n tem 5 pain ._.')


     
     



     
     