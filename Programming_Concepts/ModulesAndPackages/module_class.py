#this file uses the classes as module.
#approach 1: importing entire module
import LoanClass
home_loan = LoanClass.EMICalculator(500000, 7.5, 20)
print("Home Loan EMI(approach1):", f"{home_loan.calculate_emi():.2f}")

#approach 2: importing specific class from module
from LoanClass import CarLoanEMICalculator
car_loan = CarLoanEMICalculator(300000, 9.0, 5)
print("Car Loan EMI (approach2):", f"{car_loan.calculate_emi():.2f}")

#approach 3: importing multiple classes from module
from LoanClass import *
personal_loan = PersonalLoanEMICalculator(200000, 10.0, 3)
print("Personal Loan EMI (approach3):", f"{personal_loan.calculate_emi():.2f}")