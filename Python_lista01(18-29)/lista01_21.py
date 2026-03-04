#declaração
n1 = float(input("insira a primeira nota: "));
n2 = float(input("insira a segunda nota: "));
n3 = float(input("insira a terceira nota: "));
n4 = float(input("insira a quarta nota: "));
#inicio
media = (n1+n2+n3+n4)/4;
if(media >= 6):
    print("APROVADO");
elif(media < 3):
    print("REPROVADO");
else:
    print("EXAME");

#fim