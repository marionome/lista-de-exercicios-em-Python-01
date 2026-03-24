def mudança(preço_a,venda_m,preço_n):
    if (venda_m < 500)and(preço_a<30):
        preço_n = preço_a + (preço_a*0.10)
    elif(venda_m>=500 and venda_m<1000) and (preço_a>=30 and preço_a< 80):
        preço_n = preço_a + (preço_a*0.15)
    elif(venda_m>=1000)and(preço_a>=80):
        preço_n = preço_a - (preço_a*0.05)
    print("o preço novo é ", preço_n)

def main():
    preço_a = float(input("insira o preço atual do produto:"))
    venda_m = float(input("insira a media mensal do produto:"))
    preço_n = preço_a
    mudança(preço_a,venda_m,preço_n)

if __name__=="__main__":
    main()