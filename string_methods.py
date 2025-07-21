name = input("Enter your name: ")

result = len(name)                      #lens:- length
print(result)

print("--------------------------------")

text = "I like Python and I like Java"
index = text.find("like")
                                #find:- Finds the first occurrence of the substring

print(index)

print("---------------------------------")

text = "I like Python and I like Java"
index = text.rfind("like")
print(index)            #rfind:- Finds the last occurrence of the substring


print("-------------------------")

name = input("Enter your name: ")
name = name.capitalize()
print("This is Capitalize: ", name)

print("-------------------------")

name = input("Enter your name: ")
name = name.upper()

print("This is UPPER: ", name)

print("-------------------------")

name = input("Enter your name: ")
name = name.lower()

print("This is Lower: ", name)

print("-------------------------")

name = input("Enter your name: ")
result = name.isdigit()

print("This is isdigit: ", result)

print("-------------------------")

name = input("Enter your name: ")
result = name.isalpha()

print("This is isaplha: ", result)

print("-------------------------")

phone_number = input("Enter your phone number #: ")

result =phone_number.count("-")
print("This is count method: ", result)

print("-------------------------")

phone_number2= input("Enter your phone number: ")
phone_number2 = phone_number2.replace("-", "")

print("This is replace method; ", phone_number2)