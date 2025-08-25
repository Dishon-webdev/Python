# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.expect 3.finally


try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divided by zero IDIOT!")
except ValueError:
    print("Enter only number please!")
finally:
    print("Do some cleanup here")