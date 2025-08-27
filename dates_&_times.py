
import datetime

date = datetime.date(2035, 8, 27)

today = datetime.date.today()

time = datetime.time(9, 7, 0 )

now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

print(date)
print(today)
print(time)
print(now)

print("********************")

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")

