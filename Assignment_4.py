number = input("Enter a positive integer number : ")
tester = 0
x = number.isdigit()
if not x:
    print("Warning!! positive integer please : Run the program again")
else:
    for i in range (2, int(number)):
        if int(number) % i == 0:
            tester += 1
    if tester != 0 or int(number) <= 1:
        print("No, {} is not a prime number.".format(number))
    else:
        print("Yes, {} is a prime number.".format(number))
