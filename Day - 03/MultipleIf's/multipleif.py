print("welcome to the Roller Coster Ride")
height = int(input("enter your height: "))
bill = 0
if height > 120:
    print("you can ride")
    age = int(input("What is your age? "))
    if age <= 12:
        bill += 5
    elif age<=18:
        bill += 7
    else:
        bill += 12

    want_photos = input("Do you want photos? ")
    if want_photos == "yes":
        bill += 3 
    print(f"Your final bill is {bill}")
else:
    print("you can't ride")