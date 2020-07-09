age = str(input("Are you a cigarette addict older than 75 years old? (Yes or No) :")).title().strip()
chronic = str(input("Do you have a severe chronic disease? (Yes or No) :")).title().strip()
immune = str(input("Is your immune system too weak? (Yes or No) :")).title().strip()
risk = age or chronic or immune
if risk == "Yes":
    print("You are in risky group !!!")
else:
    print("You are not in risky group :)")
