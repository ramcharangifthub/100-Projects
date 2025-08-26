from art import logo


def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


def calculation():
    print(logo)
    a = int(input("What's the first number?: "))
    should_continue = True
    while should_continue:
        operations = {
            "+": add,
            "-": sub ,
            "*": mul,
            "/": div
        }
        for x in operations:
            print(x)
        operator = input("pick an operation: ")
        b = int(input("What's the next number?: "))

        answer = operations[operator](a,b)
        print(f"{a} {operator} {b} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: ").lower()
        if should_continue == "y":
            a = answer
        else:
            should_continue = False
            calculation()



calculation()