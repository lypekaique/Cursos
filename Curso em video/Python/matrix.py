matriz=[[], [], [], [], [], [], [], [], [],]


matriz[0].append(int(input('digite a matriz[0,0]: ' )))
matriz[1].append(int(input('digite a matriz[0,1]: ' )))
matriz[2].append(int(input('digite a matriz[0,2]: ' )))
matriz[3].append(int(input('digite a matriz[1,0]: ' )))
matriz[4].append(int(input('digite a matriz[1,1]: ' )))
matriz[5].append(int(input('digite a matriz[1,2]: ' )))
matriz[6].append(int(input('digite a matriz[2,0]: ' )))
matriz[7].append(int(input('digite a matriz[2,1]: ' )))
matriz[8].append(int(input('digite a matriz[2,2]: ' )))

print(f'{matriz[0:3]} \n {matriz[3:6]} \n {matriz[6:9]}')