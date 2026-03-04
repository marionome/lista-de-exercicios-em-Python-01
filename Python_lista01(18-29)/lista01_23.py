#declaração
v1 = int(input("Insira quatro numeros(os tres primeiros precisam esta em ordem crescente):"))
v2 = int(input())
if v1 > v2:
    print("insira os tres primeiros valores em ordem crescente")
    exit()
v3 = int(input())
if v2 > v3:
    print("insira os tres primeiros valores em ordem crescente")
    exit()
v4 = int(input())
#inicio
if v4 < v1:
    print(v4,v1,v2,v3,sep=" ")
elif v4 < v2:
    print(v1,v4,v2,v3,sep=" ")
elif v4 < v3:
    print(v1,v2,v4,v3,sep=" ")
else:
    print(v1,v2,v3,v4,sep=" ")
#fim