n1=int(input('digite o primeiro numero: '))
n2=int(input('digite o segundo numero: '))

if n1>n2:
    print('o numero 1 que é {}, é maior que o segundo numero que é {}'.format(n1,n2))
elif n2>n1:
    print('o numero 2 que é {}, é maior que o primeiro numero que é {}'.format(n2,n1))
else:
    print('ambos são os memsmo')