menu = {"Popcorn": 250.00,
    "Large Popcorn": 700.00,
    "Soda": 300.00,
    "Large Soda": 450.00,
    "Candy": 250.00,
    "Chocolate": 330.00,
    "Nachos": 450.00,
    "Hotdog": 400.00,
    "Pretzel": 340.00,
    "Ice Cream": 240.00}

cart = []
total = 0

print("------------------- MENU -------------------")
for key, value in menu.items():
    print(f"{key:20}: Rs {value:.2f}")
print("--------------------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")