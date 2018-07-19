fibo = [1, 1]

for teller in range(2, 20):
    fibo.append(fibo[teller - 1] + fibo[teller - 2])

print(fibo)
