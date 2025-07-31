# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operators
#                     1. positional 2. default 3. keyword 4. ARBITRARY

# kwargs :- keyword arguments

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 87))

print("--------------------")

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dishon", "Consalves")

print()
print("--------------------")
print("--------------------")
print("--------------------")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="Fake street", city="Mannar", state="Nothern", zip=54321,)

print("--------------------")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Mr", "Dishon", "Consalves",
               street="123 fake street",
               pobox="PO box #1001",
               city="Mannar",
               state="Nothern",
               )