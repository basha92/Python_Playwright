#using class as module
class EMICalculator:
    def __init__(self, principal, annual_rate, tenure_years):
        self.principal = principal
        self.annual_rate = annual_rate
        self.tenure_years = tenure_years

    def calculate_emi(self):
        monthly_rate = self.annual_rate / (12 * 100)  # Convert annual rate to monthly and percentage to decimal
        tenure_months = self.tenure_years * 12  # Convert years to months

        # EMI formula
        emi = (self.principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
        return emi
class CarLoanEMICalculator(EMICalculator):  #inheriting parent class attributes and functions
    def __init__(self, principal, annual_rate, tenure_years):
        super().__init__(principal, annual_rate, tenure_years)

class PersonalLoanEMICalculator(EMICalculator):
    def __init__(self, principal, annual_rate, tenure_years):
        super().__init__(principal, annual_rate, tenure_years)