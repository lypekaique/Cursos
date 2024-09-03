dia = int(input('quantos dia vc ficou com ele? '))
km = float(input('quantos km vc rodou com ele? '))


novo= (dia * 60) + (km * 0.15)

print('o valor deu {:.2f}'.format(novo))