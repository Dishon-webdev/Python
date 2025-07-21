 # logical operators = evaluate multiple conditions (or, and, not)
 #                     or = at least one condition must be True
 #                    and = both conditions must be True
 #                    not = inverts the condition (not False, not True)

temp=33
is_raining = False


if temp > 35 or temp < 0 or is_raining:
     print("The outdoor event is cancelled")
else:
     print("The outdoor event is still scheduled")

print("------------------------------------------------------")

temperature = -1
is_sunny = True

if temperature >= 28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny")
elif temperature <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 28 > temperature > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")

print("----------------------")


temper = 0
is_sunny = False

if temper >= 28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny")
elif temper <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 28 > temper > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
elif temper >= 28 and not is_sunny:
    print("It is Hot outside")
    print("It is Cloudy")
elif temper <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is Cloudy")
elif 28 > temper > 0 and not is_sunny:
    print("It is warm outside")
    print("It is Cloudy")
