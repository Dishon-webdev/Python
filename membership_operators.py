# Membership operators = used to test weather a value or variable is found in a sequence
#                        (string, list, tuples, set, or dictionary)
#                           1. in
#                           2. not in

word = "Dishon".lower()

letter = input("Guess a letter in the secret word: ")

if letter in word:
     print(f"There is a {letter}")
else:
    print(f"{letter} was not found")
    print()

print("---------------------------")

name = "Dishon"

letter2 = input("Guess a letter in the secret word: ")

if letter2 not in name:
    print(f"{letter2} was not found")
else:
    print(f"There is a {letter2}")
    print()

print("---------------------------")
print("---------------------------")

students = {"dishon", "ajith", "akachcheliyan"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")
    print()

print("---------------------------")

students = {"dishon", "ajith", "akachcheliyan"}

student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")
    print()

print("---------------------------")
print("---------------------------")

grades = {"dishon": "A", "sharon": "B", "delshan": "C", "divyni": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")
    print()

print("---------------------------")
print("---------------------------")

email = "consalvesdishon16@gmail.com"

if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")