# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

print("--------------------")

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
square = [z * z for z in range(1, 11)]

print(doubles)
print()
print(triples)
print()
print(square)

print("---------------------------")
print("---------------------------")

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"] ]
print(fruits)

print("---------------------------")

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)