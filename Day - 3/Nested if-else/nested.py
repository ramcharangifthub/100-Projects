print("welcome to the Roller Coster Ride")
height = int(input("enter your height: "))
if height > 120:
    print("you can ride")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Your ride costs $5")
    elif age<=18:
        print("your ride cost $7")
    else:
        print("Your ride costs $12")
else:
    print("you can't ride")