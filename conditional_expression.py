# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of two values based on a condition
#                          X if condition else Y

num = -6
number = 8


print ("positive" if num > 0 else "Negative")

print ("---------------------------------------------")

result = "Even" if number % 2 == 0 else "Odd"

print(result)

print ("---------------------------------------------")

a = 7
b = 18

min_num = a if a < b else b
max_num = a if a > b else b

print(min_num)
print(max_num)

print ("---------------------------------------------")
age = 18

status = "Adult" if age >= 18 else "Child"
print(status)

print ("---------------------------------------------")

temperature = 24

weather= "HOT" if temperature > 29 else "COLD"

print(weather)

print("-----------------------------------------------")

user_role = "member"

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print (access_level)

