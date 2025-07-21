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
print(name)

print("-------------------------")

name = input("Enter your name: ")
name = name.upper()

print(name)

print("-------------------------")

name = input("Enter your name: ")
name = name.lower()

print(name)

print("-------------------------")

name = input("Enter your name: ")
result = name.isdigit()

print(result)

print("-------------------------")

name = input("Enter your name: ")
result = name.isalpha()

print(result)

print("-------------------------")



