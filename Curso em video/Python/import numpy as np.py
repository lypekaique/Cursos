import numpy as np

a= np.array([[1, 1, -1],
           [6, 2, 2],
           [-3, 4, 1]], float) 

b=np.array ([-3, 2, 1 ],float)

n=len(b)

x=np.zeros(n, float)


for k in range (n-1):
    for i in range(k+1 , n):
        fctr = a[i, k] / a[k, k]
        for j in range (k, n):
            a[i, j] = a[i, j] - fctr*a[k , j]
        b[i] = b[i] - fctr*b[k]
    
    
    
    
x[n-1]= b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    sum=b[i]
    for j in range(i+1, n):
        Sum =b[i]
        for j in range(i+1, n):
            sum= sum - a[i, j]*x[j]
        x[i] = sum / a[i, i]

print(x)

