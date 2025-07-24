import time

time.sleep(3)

print("Time's up!")

print("----------------------------")

my_time = int(input("Enter the time in second: "))
for x in range(0, my_time):
    print(x)
    time.sleep(1)       #Without time.sleep(1), your loop would run super fast — all numbers would print instantly
print("Time's up!")

print("----------------------------")
print("----------------------------")
print("----------------------------")

my_time = int(input("Enter the time in second: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")