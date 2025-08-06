# Simple Python Calculator

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y


def calculator():
    print("=== Simple Calculator ===")
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Quit")

    while True:
        # Get user choice
        choice = input("\nEnter your choice (1-5): ")

        # Check if user wants to quit
        if choice == '5':
            print("Thanks for using the calculator!")
            break

        # Check if choice is valid
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")
            continue

        # Get numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        # Perform calculation based on choice
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")

        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):  # Check if it's an error message
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")


# Run the calculator
if __name__ == "__main__":
    calculator()