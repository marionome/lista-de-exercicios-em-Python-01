#declaração
v1 = int(input("Insira um valor:"))
v2 = int(input("Insira um valor:"))
soma = int(0)
#inicio
if v1 > v2:
     for i in range(v2+1, v1):
          if i%2 == 1:
               soma = soma+i
else:
    for i in range(v1+1, v2):
        if i%2 == 1:
            soma = soma+i
print(soma)
#fim