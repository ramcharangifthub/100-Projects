programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that can easily call over and over again.",
}
print(programming_dictionary["Bug"])
programming_dictionary["loop"] = "The action of doing something over and over again."

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])