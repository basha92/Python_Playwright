#compound interest calculator using while
#formula = principle*((1+rate/100)) power time

#calling required variables:
try:
    principle = float(input("Enter the amount: "))
except ValueError:
    print("Invalid Input. Please enter numeric value")
    exit()
try:
    rate = float(input("Enter rate of interest: "))
except ValueError:
    print("Invalid Input. Please enter numeric value")
    exit()
try:
    time = int(input("Enter the time period: "))
except ValueError:
    print("Invalid Input. Please enter numeric value")
    exit()

#calculation
total = principle*pow((1+rate/100), time)
print(f"Balance after {time} years: Rs.{total: .2f}")

