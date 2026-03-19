#declaração
conta = int(0)
#inicio
for i in range(1,16):
    if i%2 == 0:
      conta = conta-(i/(i*i))
    else:
       conta = conta+(i/(i*i))
print (f"{conta:.2f}")
#fim