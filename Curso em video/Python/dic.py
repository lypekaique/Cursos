aluno=dict()
aluno ['Nome'] = str(input('digite seu nome: '))
aluno ['Nota'] = float(input('digite sua nota: '))

if aluno['Nota'] >= 6:  
    print(f'seu nome é {aluno["Nome"]} sua nota é {aluno["Nota"]} Aprovado ')
else:
    print(f'seu nome é {aluno["Nome"]} sua nota é {aluno["Nota"]} Reprovado ')