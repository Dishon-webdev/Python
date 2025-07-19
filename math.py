import math

#print(math.pi)                 output: 3.141592653589793
#print(math.e)                  output: 2.718281828459045

x = 9
y = 9.4
z = 9.9

#result = math.sqrt(x)              output: 3.0
#result = math.ceil(y)              output: 10
#result = math.floor(z)             output: 9

#print(result)

print("-----------------------------------------------")

# Questions1
radius = float (input ('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

#print (f"The circumference is: {circumference}")         output: Enter the radius of a circle: 10.5
#                                                                 The circumference is: 65.97344572538566

print (f"The circumference is: {round(circumference, 2)}cm")

print ("----------------------------------------------------------")

# Question2

radius2 = float (input("Enter the radius of a circle: "))

area = math.pi * pow(radius2, 2)

print (f"The area of a circle is: {round(area, 2)}cm^2")

print ("---------------------------------------------")

#Question 3

a = float (input("Enter side A: "))
b = float (input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")