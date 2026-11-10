def print_variable(variable):
    return variable, type(variable)


x = 10
print(print_variable(x))

x = "Hello"
print(print_variable(x))

x = 5.5
print(print_variable(x))

x = True
print(print_variable(x))