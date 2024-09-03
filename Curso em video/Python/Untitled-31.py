km=int(input('digte o km: '))

if km<200:
    
    print('vc andou menos que 200 km logo vc ira pagar {} em R$'.format(km*0.50))

else:
   
    print('vc andou mais que 200 km logo vc ira pagar {} em R$'.format(km*0.45))
    