#this is a demo file for accessing the package named ModulesAndPackages
#approach 1: using the full package path - not needed much often
#import sys
#sys.path.append('F:\Python_Git\Python_Playwright\ModulesAndPackages')
  
# directly using the package path to import the module
#import ModulesAndPackages.EMI as emi_pkg  #mention the package name along with module name
#home_loan_emi_pkg = emi_pkg.calculate_emi(4000000, 7.2, 25)
#print(f"Home Loan EMI (using package path): {home_loan_emi_pkg:.2f}")

#approach 2: using __init__.py file in the package to simplify the imports
#from ModulesAndPackages import EMI  #importing module using package name
#home_loan_emi_pkg2 = EMI.calculate_emi(4000000, 7.2, 25)
#print(f"Home Loan EMI (using __init__.py): {home_loan_emi_pkg2:.2f}")

#approach 3: importing specific functions from module in the package
#from ModulesAndPackages.LoanClass import EMICalculator, CarLoanEMICalculator, PersonalLoanEMICalculator
#home_loan = EMICalculator(500000, 7.5, 20)
#print("Home Loan EMI (approach3):", f"{home_loan.calculate_emi():.2f}")
#car_loan = CarLoanEMICalculator(300000, 9.0, 5)
#print("Car Loan EMI (approach3):", f"{car_loan.calculate_emi():.2f}")
#personal_loan = PersonalLoanEMICalculator(200000, 10.0, 3)
#print("Personal Loan EMI (approach3):", f"{personal_loan.calculate_emi():.2f}")

#approach 4: using package inside package
from ModulesAndPackages.StudentPackage.StudentDetails import get_student_details
student_id = 2
student_info = get_student_details(student_id)
print(f"Details of student with ID {student_id}: {student_info}")

from ModulesAndPackages.StudentPackage.StudentDetails import get_student_details
student_id = 5
student_info = get_student_details(student_id)
print(f"Details of student with ID {student_id}: {student_info}")

from ModulesAndPackages.LoanClass import EMICalculator
home_loan = EMICalculator(500000, 7.5, 20)
print("Home Loan EMI:", f"{home_loan.calculate_emi():.2f}")