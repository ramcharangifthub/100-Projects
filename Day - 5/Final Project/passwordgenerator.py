import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welome to Password Generator program")

nr_letters = int(input("How many letters would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))

password = ""
for x in range(1,nr_letters+1):
    password += random.choice(letters)
for y in range(1,nr_numbers+1):
    password += random.choice(numbers)
for z in range(1,nr_symbols+1):
    password += random.choice(symbols)
print(f"your easy password is {password}")

password_list = [ ]
for x in range(1,nr_letters+1):
    password_list.append(random.choice(letters))
for y in range(1,nr_numbers):
    password_list.append(random.choice(numbers))
for z in range(1,nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password1 = ""
for char in password_list:
    password1 += char
print(f"your hardest password is {password1}")