import math
angulo=float(input('digite o angulo: '))
seno= math.sin(math.radians(math.ceil(angulo)))
cos= math.cos(math.radians(math.ceil(angulo)))
tan= math.tan(math.radians(math.ceil(angulo)))

print('o angulo digitado foi:{:.2}, \n o seno desso angulo é {:.2} \n o cos é {:.2} \n e o tan é {:.2}'.format(angulo,seno,cos,tan))
