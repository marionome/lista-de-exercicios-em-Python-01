def media():
    media = (n1+n2+n3+n4)/4;
    if(media >= 6):
        print("APROVADO");
    elif(media < 3):
        print("REPROVADO");
    else:
        print("EXAME");

def main():
    global n1
    global n2
    global n3
    global n4
    n1 = float(input("insira a primeira nota: "));
    n2 = float(input("insira a segunda nota: "));
    n3 = float(input("insira a terceira nota: "));
    n4 = float(input("insira a quarta nota: "));
    media();
if __name__ == "__main__":
    main()