#this file has basic employee details module inside EmployeePackage
class Employee:
    def __init__(self, first, last, pay):
        self.first = first  #instance variable
        self.last = last    #instance variable
        self.pay = pay      #instance variable
        self.email = '{}.{}@company.com'.format(first, last)  #instance variable
    def fullname(self):
        return '{} {}'.format(self.first, self.last)