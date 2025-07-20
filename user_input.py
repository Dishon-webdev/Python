# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = input ("How old are you?: ")

age = int(age)
age = age + 1

print (f"Hello {name}!")
print ("Happy birthday")
print (f"I am {age} years old")

print ("-------------------------------------------")

#  Exercise 1 Rectangle area calc

length = float (input("Enter the length: "))
width = float (input ("Enter the width: "))
area = length * width

print(f"The area is: {area}")

print ("----------------------------------------------------")

# Exercise 2 Shopping card programme

item = input("What item would you like to buy?: ")
price = float ( input ("What is the price?: "))
quantity = int ( input ("How many would you like to buy?:  "))
total = price * quantity

print (f"You have bought {quantity} x {item}/s")
print (f"Your total is ${total}")
