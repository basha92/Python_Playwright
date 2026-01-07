#this file is to access the following details:
#importing the packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

#1. student details from StudentPackage inside ModulesAndPackages package
from ModulesAndPackages.StudentPackage.StudentDetails import get_student_details
def display_student_info(student_id):
    details = get_student_details(student_id)
    print(f"student details for the ID {student_id}: {details}")
display_student_info(3) #pass the value to the called function

#2. EMI calculation from LoanClass module inside ModulesAndPackages package
from ModulesAndPackages.LoanClass import EMICalculator
home_loan = EMICalculator(1000000, 8.75, 25)
print(f"Home loan EMI: {home_loan.calculate_emi():.2f}") #call which method to be executed if using class

#3. employee details from EmployeeDetails module inside EmployeePackage
from EmployeePackage.EmployeeDetails import Employee
emp1 = Employee('Sikkandar', 'Basha', '15000')
print(f"""Employee details: 
      Name : {emp1.fullname()}
      email: {emp1.email}""")