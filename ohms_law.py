# ohms_law.py

# Ask the user for current (I) and resistance (R)
try:
    current = float(input("Enter the current (in A): "))
    resistance = float(input("Enter the resistance (in ohms): "))

    # Calculate voltage using Ohm's Law: V = I * R
    voltage = current * resistance

    # Display the result
    print(f"The voltage is: {voltage} volts")

except ValueError:
    print("Please enter valid numeric values for current and resistance.")
