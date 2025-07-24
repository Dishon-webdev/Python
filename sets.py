# set  = {} unordered and immutable, but Add/Remove Ok. No duplicates

fruits = {"apple", "banana", "mango", "orange"}

print(fruits)

print(dir(fruits))

print(len(fruits))

print("banana" in fruits)

fruits.add("pineapple")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)