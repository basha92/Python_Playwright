#this file use all the EMI calculations from EMI module
#approach 1: import entire module
import EMI
home_loan_emi = EMI.calculate_emi(5000000, 7.5, 20)
print(f"Home Loan EMI: {home_loan_emi:.2f}")
car_loan_emi = EMI.calculate_car_emi(1000000, 9.0, 5)
print(f"Car Loan EMI: {car_loan_emi:.2f}")
personal_loan_emi = EMI.calculate_personal_emi(500000, 12.0, 3)
print(f"Personal Loan EMI: {personal_loan_emi:.2f}")

#approach 2: import specific functions from module
from EMI import calculate_emi, calculate_car_emi, calculate_personal_emi
home_loan_emi2 = calculate_emi(6000000, 7.0, 15)
print(f"Home Loan EMI (approach 2): {home_loan_emi2:.2f}")
car_loan_emi2 = calculate_car_emi(1500000, 8.5, 4)
print(f"Car Loan EMI (approach 2): {car_loan_emi2:.2f}")
personal_loan_emi2 = calculate_personal_emi(700000, 11.5, 2)
print(f"Personal Loan EMI (approach 2): {personal_loan_emi2:.2f}")

#approach 3: import all functions from module
from EMI import *
home_loan_emi3 = calculate_emi(7000000, 6.5, 10)
print(f"Home Loan EMI (approach 3): {home_loan_emi3:.2f}")
car_loan_emi3 = calculate_car_emi(2000000, 8.0, 3)
print(f"Car Loan EMI (approach 3): {car_loan_emi3:.2f}")
personal_loan_emi3 = calculate_personal_emi(800000, 10.5, 1)
print(f"Personal Loan EMI (approach 3): {personal_loan_emi3:.2f}")
