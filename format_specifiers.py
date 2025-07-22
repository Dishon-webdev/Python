# format specifiers = {value:flags} format a value based on what
#                           flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


print("--------------------------------------")
# format specifiers = {value:flags} format a value based on what
#                           flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price is ${price1:.3f}")            #decimal point specifier
print(f"Price is ${price2:.3f}")
print(f"Price is ${price3:.3f}")

print("---------------------------------")
print("---------------------------------")

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price is ${price1:10}")           #it makes total 10 spaces
print(f"Price is ${price2:10}")
print(f"Price is ${price3:10}")

print("-----------------------------------")
print("-----------------------------------")

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price is ${price1:010}")        # zero padded
print(f"Price is ${price2:010}")
print(f"Price is ${price3:010}")

print("-----------------------------------")
print("-----------------------------------")

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price is ${price1:<10}")            #left align (spaces)
print(f"Price is ${price2:<10}")
print(f"Price is ${price3:<10}")

print("-----------------------------------")
print("-----------------------------------")

print(f"Price is ${price1:>10}")            #right align
print(f"Price is ${price2:>10}")
print(f"Price is ${price3:>10}")

print("-----------------------------------")
print("-----------------------------------")

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price is ${price1:^10}")
print(f"Price is ${price2:^10}")
print(f"Price is ${price3:^10}")                #center align

print("-----------------------------------")
print("-----------------------------------")

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price is ${price1:+}")
print(f"Price is ${price2:+}")
print(f"Price is ${price3:+}")              #positive numbers

print("-----------------------------------")
print("-----------------------------------")

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price is ${price1: }")
print(f"Price is ${price2: }")
print(f"Price is ${price3: }")          #insert a space before positive numbers

print("-----------------------------------")
print("-----------------------------------")

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price is ${price1:,}")
print(f"Price is ${price2:,}")
print(f"Price is ${price3:,}")              #comma separator

print("-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price is ${price1:+,.2f}")
print(f"Price is ${price2:+,.2f}")
print(f"Price is ${price3:+,.2f}")