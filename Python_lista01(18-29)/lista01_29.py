#Modulo
def calc(tipo, valor_i):
    if tipo == 1:
        valor_i = valor_i+(valor_i*0.03)
        print("o valor apos 30 dias:",valor_i)
    elif tipo == 2:
        valor_i = valor_i+(valor_i*0.05)
        print("o valor apos 30 dias:", valor_i)
    else:
        print("Tipo de investimento invalido,insira um tipo de investimento valido")

def main():
    tipo = int(input("insira o tipo de investimento(1 para poupança e 2 para renda fixa):"))
    valor_i = float(input("insira o valor do investimento:"))
    calc(tipo, valor_i)

if __name__ == "__main__":
    main()
