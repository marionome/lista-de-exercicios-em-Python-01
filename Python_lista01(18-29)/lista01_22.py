
def ordem():
    if(v1 == v2):
        print("Os dois valores são iguais, insira novamente.");
    elif (v1 > v2):
        print(v1,v2,sep=" ")
    else:
        print(v2,v1,sep=" ")

def main():
    global v1
    global v2
    v1 = int(input("Insira o primeiro valor: "));
    v2 = int(input("Insira o segundo valor: "));
    ordem()

if __name__ == "__main__":
    main()