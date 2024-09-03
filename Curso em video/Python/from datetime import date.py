from datetime import date

ano= int(input('que ano quer analisar? ou 0 para analisar seu ano '))
if ano == 0:
    ano = date.today().year
if ano %4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('o ano {} é bisexo'.format(ano))
else:
    print('o ano {} não é bisexo'.format(ano))