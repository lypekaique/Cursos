print('-='*30)
print(f'irei fazer algumas perguntas... espero que responde com sinceridade \n responde 1 para sim e 0 para não')
print('-='*30)

per = []
per.append(input(f"Telefonou para a vítima? \n Sim ou Não: "))
per.append(input(f"Esteve no local do crime? \n  Sim ou Não: "))
per.append(input(f"Mora perto da vítima? \n Sim ou Não: "))
per.append(input(f"Devia para a vítima? \n Sim ou Não: "))
per.append(input(f"Já trabalhou com a vítima? \n Sim ou Não: "))
Contador = 0

    
for i in per: 
 Contador += int(i)
if (Contador < 2):
  print(f"Ta safe \n voce tem isso: {Contador} de provas")
elif (Contador == 2):
  print(f"S U S P E I T O  \n voce tem isso: {Contador} de provas ")
elif (3 <= Contador <= 4):
  print(f"sei não essa bosta ta fedendo \n voce tem isso: {Contador} de provas")
else :
  print(f"É TU NÉ VIADO TODAS AS 5 Provas ta em tu ")
