import datetime

ano=int(input('digite seu ano de nascimento: '))
date = datetime.date.today()
ano2 = int(date.strftime("%Y"))


if (ano2-ano)<18:
    print('ta safe ainda falta {}'.format((ano2-ano-18)))
elif (ano2-ano)>18:
    print('o pior ja passou voce tem {}'.format (ano2-ano-18))
else:
    print('fudeo bahia TU TEM 18')







