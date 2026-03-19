#declaração
pista_t = float(input("Insira o tamanho da pista(em metros):"))
voltas = int(input("Insira a quantidade de voltas:"))
tempo = int(input("insira o tempo que levou(em minutos):"))
#inicio
Vel_media = (pista_t * voltas)/tempo
print("A velocidade media foi de ", Vel_media*3.6,"km/h")
#fim