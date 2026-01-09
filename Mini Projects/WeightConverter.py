#kg to pounds vice versa.
#1 kg = 2.20462 pound
try:
    weight = float(input("Enter your weight:"))
except ValueError:
    print("Invalid Input. Please enter numeric value")
    exit()

unit = input('Kilograms or Pounds (K/L):')

if unit == 'K':
    weight = round((weight*2.20462),3)
    unit = "Lbs."
elif unit == 'L':
    weight = round((weight/2.20462),3)
    unit = "Kgs."
else:
    print(f"{unit} was not valid")
    exit()

print(f"Your weight is: {weight} {unit}")