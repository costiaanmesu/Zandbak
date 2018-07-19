fibonaci = [1, 1]

for teller in range(2, 15):
    fibonaci.append(fibonaci[teller-1]+fibonaci[teller-2])

print(fibonaci)
