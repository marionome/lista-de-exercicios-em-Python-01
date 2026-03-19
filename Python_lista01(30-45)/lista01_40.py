#declaração
v1 = int(input("insira um valor:"))
v2 = int(input("insira um valor:"))
contador= int(0)
#inicio
if v1 > v2:
    for i in range(v2+1,v1):
        for p in range(1,i+1):
            if i%p == 0:
                contador+=1
        if contador == 2:
         print(i)
        contador = 0
elif v2>v1:
    for i in range(v1+1,v2):
        for p in range(1,i+1):
         if i%p == 0:
            contador+=1
        if contador == 2:
            print(i)
        contador = 0
else:print("você inseriu dois valores iguais")
#fim