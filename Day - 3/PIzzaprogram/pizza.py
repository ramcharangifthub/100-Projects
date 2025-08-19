print("Welcome to Pizza Delivary")
size = input("what size of pizza do you want?(s,m, or l):  ").lower()
peproni = input("Do you want peproni?('y' or 'n'): ")
cheese = input("Do you want cheese?('y' or 'n'): ")
bill = 0

if size == "s":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25 
else:
    print("you have entered a wrong input.")


if peproni == 'y':
    if size == "s":
        bill += 2
    else:
        bill += 3

if cheese == "y":
    bill += 2

print(f"Your total bill for the pizza is {bill}")