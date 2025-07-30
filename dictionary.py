# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "Sri Lanka": "Colombo",
            "China": "Beiging",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("India"))
print(capitals.get("Sri Lanka"))

print("---------------------------")

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exists")

print("--------------------------")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})         #Can update existing also
print(capitals)

print("--------------------------")

capitals.pop("China")

print(capitals)
print("--------------------------")

capitals.popitem()              #Removes the last / latest key & value
print(capitals)

print("--------------------------")

keys = capitals.keys()           #Shows only the key values
print(keys)

print("--------------------------")

for key in capitals.keys():
    print(key)

print("--------------------------")

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

print("--------------------------")

items = capitals.items()

print(items)
print("--------------")
for key, value in capitals.items():
    print(f"{key}: {value}")
print("--------------------------")
print("--------------------------")

capitals.clear()                #Clear all the values & keys
print(capitals)

print("--------------------------")

