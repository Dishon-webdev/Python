# Tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits = ("apple", "banana", "orange", "mango")

print(fruits)
print("--------------------")
print(dir(fruits))
print("--------------------")
print(len(fruits))
print("--------------------")

print("pineapple" in fruits)
print("--------------------")

print(fruits.index("apple"))
print("--------------------")
print(fruits.count("banana"))

print("--------------------")

for fruit in fruits:
    print(fruit)