#declaração
th = float(input("insira o numero de horas trabalhadas:"));
vh = float(input("insira o valor da hora trabalhada:"));
d = float(input("insira o percentual de desconto:"));
nd = float(input("insira o numero de dependentes:"));
#inicio
sb = th * vh;
sl = (sb -(sb*(d/100))) + (nd * 100);
print("o valor do salario liquido é:", sl);
#fim