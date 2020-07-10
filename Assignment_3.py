result = 0          # isdigit() kullanılarak sorgulama yapıldı.
a = 0
number = input("Enter a positive integer number :")   
x = number.isdigit()

while not x:
    print("warning!!! Enter in right format")
    number = input("Enter a positive integer number :")
    x = number.isdigit()     
else:
    for i in str(number):
        a += 1
    for i in str(number):
        result += int(i)**a
    if result == int(number):
        print(result)
        print("Yes the number {} is an Armstrong Number".format(number))
    else:
        print("No the number {} is not an Armstrong Number!!!".format(number))
