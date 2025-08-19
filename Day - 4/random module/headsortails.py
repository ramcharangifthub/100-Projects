import random 
import my_module

random_number = random.randint(1,10)
print(random_number)

random_float = random.random()
print(random_float)

print(my_module.my_favourite_number)

# Heads or Tails
print("Welcome to Heads or Tails Program")

number = random.randint(0,1)
if number == 0:
    print("Heads")
else:
    print("Tails")