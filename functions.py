# function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Dishon", 22)
happy_birthday("Sharon", 19)
happy_birthday("Rutvika", 4)



print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Dishon", 22000, "01/01")