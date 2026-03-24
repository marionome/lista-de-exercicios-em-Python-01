def divisivel():
    if(v%2 == 0 and v%3 == 0):
        print("O numero é divisivel por 2 e por 3");
    elif(v%2 == 0):
        print("O numero é divisivel por 2");
    elif(v%3 == 0):
        print("O numero é divisivel por 3");
    else:
        print("não é divisivel por nenhum dos dois")

def main():
    global v
    v = int(input("insira um valor: "));
    divisivel()

if __name__ == "__main__":
    main()
