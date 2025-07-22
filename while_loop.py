# while loop = execute some code WHILE some condition remain true

name = input(f"Enter your name: ")

while name == "":
    print("you did not enter your name")
    name = input(f"Enter your name: ")
print(f"Hello {name}")

print("------------------------------")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"Your are {age} years old")