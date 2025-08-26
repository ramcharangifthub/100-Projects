def function_name(f_name,l_name):
    if f_name == "" and l_name == "":
        return "You did not entered a valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(function_name(f_name=input("what is your first name?"),l_name=input("what is your last name?")))