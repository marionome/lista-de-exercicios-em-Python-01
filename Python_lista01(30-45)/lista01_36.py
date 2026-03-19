#declaração
n = int(input("insira um numero:"))
serie=0
fatorial=1
#inicio
for i in range(1,n+1):
    serie = serie + (1/(i*fatorial))
    fatorial = fatorial * i
print(serie)
#fim