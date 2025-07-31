# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. DEFAULT 3. KEYWORD 4. arbitrary

def hello(greetings, title, first, last):
    print(f"{greetings} {title} {first} {last}")

hello("Hello!", "Mr.", "Dishon", "Consalves")

hello(greetings="Hello!", title="Mr.", first="Dishon", last="Consalves")

print("-------------------------")
print("-------------------------")


for x in range(1, 11):
    print(x, end=" ")

print()
print("------------------")

print("1", "2", "3", "4", "5", sep="-")

print("----------------")
print("----------------")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=94, area=76, first="0410", last=620)
# In Python, numbers can’t start with 0 (like 0620) — it causes an error.

print(phone_num)