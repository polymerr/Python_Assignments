year = int(input("enter a year if is that leap year or not :"))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(f"No, entered value {year} is NOT a prime number")
    else:
        print(f"Yes, entered value {year} is a prime number")

else:
    print(f"No, entered value {year} is NOT a prime number")
