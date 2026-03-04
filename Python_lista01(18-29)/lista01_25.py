#declaração
h1 = int(input("insira as horas que o jogo começou: "));
if h1 < 0 or h1 > 24:
    print("insira um valor entre 0 e 24");
    exit();
m1 = int(input("insira os minutos que o jogo começou: ")); 
if m1 < 0 or m1 > 60:
    print("insira um valor entre 0 e 60");
    exit();
h2 = int(input("insira as horas que o jogo terminou: "));
if h2 < 0 or h2 > 24:
    print("insira um valor entre 0 e 24");
    exit();
m2 = int(input("insira os minutos que o jogo terminou: "));
if m2 < 0 or m2 > 60:
    print("insira um valor entre 0 e 60");
    exit();
#inicio
hf = h2 - h1;
mf = (m2 - m1);
if mf < 0:
    hf = hf - 1;
    mf = mf + 60;
print(hf," horas e ",mf," minutos"); 
#fim