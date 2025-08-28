try:
    age = int(input("what is your age? "))
except ValueError:
    print("You have typed an invalid number.Please try again with a numberical like '14'.")
    age = int(input("what is your age? "))
if age > 18:
    print(f"you can drive at age {age}")