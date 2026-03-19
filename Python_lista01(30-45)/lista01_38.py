#declaração
maior = int()
menor = int(input("insira um valor(apenas valores positivos): "))
n = int()
#inicio
for i in range(10):
    n = int(input("insira um valor: "))
    if n > maior and n>=0:
        maior=n
    elif n<menor and n>=0:
        menor=n
print(f"o maior valor inserido é {maior} e o menor é {menor}")
#fim