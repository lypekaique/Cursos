cadastro= list()
cadastro2= list()
mai = men = 0   
while True:
    cadastro2.append(str(input('Digite seu nome: ')))
    cadastro2.append(float(input('Digite seu peso: ')))
    if len(cadastro) == 0:
        mai = men = cadastro2[1]
    else:
        if cadastro2[1] > mai:
            mai = cadastro2[1]
        if cadastro2[1] < men:
            men = cadastro2[1]
    res=input('Quer continuar? (s ou n)')
    cadastro.append(cadastro2[:])
    cadastro2.clear()
    if res in 'nN':
        break
print('-='*30)
print(f'foram {len(cadastro)} cadastrados')
print(f'o peso maior é {mai}')
print(f'o peso menor é {men}')
    
 