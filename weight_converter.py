# Python Weight Converter


weight = float(input("Enter your weight: "))

# Get unit (K or L), and convert to uppercase for consistency
unit = input("Kilograms or Pounds? (K or L): ").upper()


if unit == "K":
    weight = weight * 2.205
    print(f"Weight in LBS: {weight:.2f}")
elif unit == "L":
    weight = weight / 2.205
    print(f"Weight in Kilograms: {weight:.2f}")
else:
    print(f"'{unit}' is not a valid option. Please enter 'K' or 'L'.")
