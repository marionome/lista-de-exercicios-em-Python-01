def multi():
    if(v1 > v2):
        if(v1%v2 == 0):
            print("o primeiro valor é multiplo do segundo")
        else: print("os valores não tem nada em comum")
    else:
        if(v2%v1 == 0):
            print("o segundo valor é multiplo do primeiro")
        else: print("os valores não tem nada em comum")

def main():
    global v1
    global v2
    v1 = int(input("Insira o primeiro valor:"))
    v2 = int(input("Insira o segundo valor:"))
    multi()

if __name__ == "__main__":
    main()