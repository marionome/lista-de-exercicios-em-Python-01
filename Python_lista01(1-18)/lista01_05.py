#declaração
A = int(input("Insira o valor do 1 numero: "));
B = int(input("Insira o valor do 2 numero: "));
C = int(input("Insira o valor do 3 numero: "));
#inicio
if (B**2 - 4 * A * C) > 0:
    print("X =", (-B + (B**2 - 4 * A * C)**(1/2)) / (2 * A));
    print("Y =", (-B - (B**2 - 4 * A * C)**(1/2)) / (2 * A));
else:
    print("A equação não possui raízes reais");
#fim