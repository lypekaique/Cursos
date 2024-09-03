nome=input('digite seu nome completo: ').strip()
print('seu nome maisculu é {} '.format((nome.upper())))
print('seu nome miusculu é {} '.format((nome.lower())))
print('seu nome tem tudo isso de letras {}'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {}'.format(nome.find(' ')))


