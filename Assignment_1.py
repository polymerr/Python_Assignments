password = "qwert1234"
name = input("Enter your name please :").title().strip()
if name == "Muhammet":
    print("Hello, {}! The password is : {}".format(name, password))
else:
    print("Hello, {}! See you later.".format(name))
