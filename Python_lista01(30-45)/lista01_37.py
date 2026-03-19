#declaração
n = int(input("insira um valor:"))
f1 = int(0)
f2 = int(1)
show = int(0)
#inicio
for i in range(1,n):#achar um jeito da sequencia inicial ser 0,1,1,2
    print(show)
    show = f1+f2
    f1 = f2;
    f2 = show
#fim