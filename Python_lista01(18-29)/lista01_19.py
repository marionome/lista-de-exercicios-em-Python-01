def maior():
    if(v1 > v2):
        print(v1," é maior que ", v2);
    elif(v1 == v2):
        print("os dois valores são iguais");
    else:
        print(v2," é maior que ", v1);

def main():
    global v1
    global v2
    v1 = int(input("insira o primeiro valor: "));
    v2 = int(input("insira o segundo valor: "));
    maior();

if __name__ == "__main__":
    main()
