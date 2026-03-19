#declaração
base = int(input("Insira o valor da base:"))
potencia = int(input("Insira o valor da potencia:"))
valor = 1
#inicio
for i in range(1,potencia+1):
    valor = valor*base 
print(valor)
#fim