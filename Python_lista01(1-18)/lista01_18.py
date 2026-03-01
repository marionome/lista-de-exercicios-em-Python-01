#declaração
v1 = int(input("Insira o primeiro numero: "));
v2 = int(input("Insira o segundo numero: "));
#inicio
if v1 > v2:
    d = v1 - v2;
    print("o valor da diferença é:", d);
else:
    d = v2 - v1;
    print("o valor da diferença é:", d);
#fim