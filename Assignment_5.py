start = 1
fibo = [1]
for i in range(8):
    start = start + fibo[i]
    fibo.append(start)
    start = fibo[i]

fibo.insert(0,1)
fibo
