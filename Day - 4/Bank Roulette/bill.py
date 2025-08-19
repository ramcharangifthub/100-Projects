import random
print("Welcome to whoose gonna pay the bill program")
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#method 1
random_name = random.choice(friends)

print(random_name)
#method 2 
random_number = random.randint(0,4)

bill = friends[random_number]
print(bill)