son = int(input("enter the ending number for prime search limit :"))
prime = []
for i in range(2, son+1):
    for ii in range(2,i):
        if i % ii == 0:
            break
    else:
        prime.append(i)

print(f"Prime list up to {son} is :", prime, sep = "\n")
