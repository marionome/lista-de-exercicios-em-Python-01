
def calc(espaço,volta,tempo):
    Vel_media = (espaço * volta)/tempo
    print("A velocidade media foi de ", Vel_media*3.6,"km/h")

def main():
    pista_t = float(input("Insira o tamanho da pista(em metros):"))
    voltas = int(input("Insira a quantidade de voltas:"))
    tempo = int(input("insira o tempo que levou(em minutos):"))
    calc(pista_t,voltas,tempo)

if __name__ == "__main__":
    main()