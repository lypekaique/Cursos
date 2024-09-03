n1=float(input('Digite sua primeira nota:  '))
n2=float(input('Digite sua segunda nota:  '))
n3=float(input('Digite sua terceira nota:  '))

media=float(n1+n2+n3)/3
print('Vc tirou {:.1f} , {:.1f} e {:.1f} , a média do aluno {:.1f}'.format(n1, n2, n3, media))      

if media >=7:
    print('Boa garotão vc passou')
elif 6.9 > media ==5 :
    print('te vejo na recupersaum')

elif media <5:
    print('R E P R O V A D O, otario ')

else:
    print('nota errada parseiro TA DE SACANAGEM?')
    