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

print("------------------------------")

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("Bye")

print("------------------------------")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")