# ohms_law.py

try:
    current = float(input("Enter the current (in A): "))
    print(f"You entered current: {current} A")

    resistance = float(input("Enter the resistance (in ohms): "))
    print(f"You entered resistance: {resistance} ohms")

    voltage = current * resistance
    print(f"The voltage is: {voltage} volts")

except ValueError:
    print("Please enter valid numeric values for current and resistance.")
