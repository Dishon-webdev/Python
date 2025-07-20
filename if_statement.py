# if = Do some code only IF some condition is True
#      Else do something else

age = int (input("Enter your age: "))


if age >=100:
    print("You are too old to sign up ")
elif age>=18:
    print("You are now signed up!")
elif age < 0:
    print("You are not born yet dumb idiot ")
#elif age >= 100:
  #  print("You are too old to sign up")
else:
    print("You must be 18+ to sign up")

print ("-------------------------------------------------")

response = input("would you like food ? (Y/N): ")
if response == "Y":
    print("Hae some food")
else:
    print("No food for you")

print ("-------------------------------------------------")

name = input("Enter your name: ")


if name == "":
    print("You did not type your name")
else:
    print(f"Hello {name}")

print ("-------------------------------------------------")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

print ("-------------------------------------------------")

online = False

if online:
    print("The user is online")
else:
    print("The user is offline")