# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(3, 3))
print(subtract(3, 3))
print(multiply(3, 3))
print(divide(3, 3))

print("---------------------")
print("---------------------")
print("---------------------")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("dishon", "consalves")

print(full_name)