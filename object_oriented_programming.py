# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car             # check it in car.py

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "white", True)
car3 = Car("Charger", 2022, "black", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print("*************")

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print("*************")
print("*************")

car2.drive()
car1.drive()
car3.drive()

print("-------------------")

car1.stop()
car2.stop()
car3.stop()

print("*******************")
print("*******************")

car1.describe()
car2.describe()
car3.describe()