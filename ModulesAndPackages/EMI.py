#using function as module
#home loan EMI calculator
def calculate_emi(principal, annual_rate, tenure_years):
    monthly_rate = annual_rate / (12 * 100)  # Convert annual rate to monthly and percentage to decimal
    tenure_months = tenure_years * 12  # Convert years to months

    # EMI formula
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    return emi

#Car loan EMI calculator
def calculate_car_emi(principal, annual_rate, tenure_years):
    monthly_rate = annual_rate / (12 * 100)  # Convert annual rate to monthly and percentage to decimal
    tenure_months = tenure_years * 12  # Convert years to months

    # EMI formula
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    return emi

#Personal loan EMI calculator
def calculate_personal_emi(principal, annual_rate, tenure_years):   
    monthly_rate = annual_rate / (12 * 100)  # Convert annual rate to monthly and percentage to decimal
    tenure_months = tenure_years * 12  # Convert years to months

    # EMI formula
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    return emi