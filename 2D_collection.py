
fruits =        ["apple", "orange", "banana", "coconut"]
vegetables =    ["celery", "carrots", "potatoes"]
meats =         ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

#fruits[0] = "pineapple"            output :- ['pineapple', 'orange', 'banana', 'coconut']
print(fruits)
print(groceries)

print("------------------------------------")

print(groceries[0])             #output :- ['apple', 'orange', 'banana', 'coconut']
print(groceries[0][0])          #output :- apple
print(groceries[0][2])          #output :- banana
print(groceries[2][2])          #output :- turkey


print("----------------------------------------")

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
