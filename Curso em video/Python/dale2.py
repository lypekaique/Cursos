n=int(input('digite um numero para ser dividido por pares:'))

for i in range (0, n+1):
    if i % 2 == 0:
        print(i, end='. ')
print('acabou')
        