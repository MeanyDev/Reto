# Reto con while
i=3
suma=0
while i<=1000:
    if i%3==True or i%5==True:
       suma+=(i-1)
    i+=1
print(suma)

# Reto con for
suma=0
for i in range(3,1001):
    if i%3==True or i%5==True:
       suma+=(i-1)
print(suma)