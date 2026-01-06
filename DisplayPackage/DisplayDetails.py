#this file is to access the following details:
#1. student details from StudentPackage inside ModulesAndPackages package
#2. EMI calculation from LoanClass module inside ModulesAndPackages package
#3. employee details from EmployeeDetails module inside EmployeePackage

from ModulesAndPackages.StudentPackage.StudentDetails import get_student_details

student_id = 3
student_info = get_student_details(student_id)
print(f"Details of student with ID {student_id}: {student_info}")

from ModulesAndPackages.LoanClass import EMICalculator
home_loan = EMICalculator(500000, 7.5, 20)
print("Home Loan EMI:", f"{home_loan.calculate_emi():.2f}")

from EmployeePackage.EmployeeDetails import Employee
emp1 = Employee('John', 'Doe', 60000)
print(f"Employee: {emp1.fullname()}, Email: {emp1.email}, Pay: {emp1.pay}")