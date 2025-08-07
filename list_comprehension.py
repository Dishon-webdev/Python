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
print("---------------------------")


numbers = [1, -1, 3, -4, 5, -6, 8, 10, -12, -16, 7, 9]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <  0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for  num in numbers if num % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

print("------------------------------")

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades]

print("---------------------------")

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)