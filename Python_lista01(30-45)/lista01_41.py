#declaração
#inicio
print("Todas as possibilidades da soma de dois dados distintos darem 7:")
for d in range(1,7):
    for i in range(1,7):
        if d+i == 7:
            print(f"{d},{i}")
#fim