# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start: end: stop]

credit_number = "1234-567-890"

print(credit_number[2])

print("-------------------------------------------------")

credit_number = "1234-567-890"

print(credit_number[0:4])

print("---------------------------------------------")

credit_number = "1234-567-890"

print(credit_number[5:8])

print("---------------------------------------------")
print("---------------------------------------------")

credit_number = "1234-567-890"

print(credit_number[5:])

print("---------------------------------------------")
print("---------------------------------------------")

credit_number = "1234-567-890"

print(credit_number[-2])

print("---------------------------------------------")
print("---------------------------------------------")

credit_number = "1234-567-890"

print(credit_number[::3])                 #it will print every 3nd numbers

print("---------------------------------------------")
print("---------------------------------------------")

credit_number = "1234-567-890"

last_digits = credit_number[-3:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

print("---------------------------------------------")
print("---------------------------------------------")

credit_number = "1234-567-890"

credit_number = credit_number[::-1]
print(credit_number)                #it prints backwards