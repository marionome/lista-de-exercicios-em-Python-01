def diferenca():
    if v1 > v2:
        d = v1 - v2;
        print("o valor da diferença é:", d);
    else:
        d = v2 - v1;
        print("o valor da diferença é:", d);

def main():
    global v1
    global v2
    v1 = int(input("Insira o primeiro numero: "));
    v2 = int(input("Insira o segundo numero: "));
    diferenca();

if __name__ == "__main__":
    main()
