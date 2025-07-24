# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates  Ok.
# set  = {} unordered and immutable, but Add/Remove Ok. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster


fruits = ["Apple", "Orange", "Banana", "Mango"]

print(fruits)
print(fruits[2])
print(fruits[::2])
print(fruits[-1])

print("-------------------------")
for x in fruits:
    print(x)

print("------------------------")

for fruit in fruits:
    print(fruit)

print("------------------------------")

print(dir(fruits))

print("------------------------------")

print(help(fruits))

print("------------------------------")
print("------------------------------")

print(len(fruits))

print("------------------------------")
print("------------------------------")

print("Apple" in fruits)
print("Pineapple" in fruits)

print("------------------------------")
print("------------------------------")

fruitsss = ["Apple", "Orange", "Banana", "Mango"]

fruitsss[0] = "Pineapple"

for fruitt in fruitsss:
    print(fruitt)

print("------------------------------")
print("------------------------------")

fruitsss = ["Apple", "Orange", "Banana", "Mango"]

fruitsss.append("Pineapple")
print(fruitsss)

fruitsss.remove("Apple")
print(fruitsss)

fruitsss.insert(0, "Pineapple")
print(fruitsss)

fruitsss.sort()
print(fruitsss)

fruitsss.reverse()
print(fruitsss)

print(fruitsss.index("Mango"))

print(fruitsss.count("Banana"))

fruitsss.clear()
print(fruitsss)

