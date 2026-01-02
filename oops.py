#class, object, inheritance, polymorphism
#class - A blueprint for creating objects. It defines a set of attributes(variables) and methods that the created objects will have.
#object - An instance of a class. It is created using the class blueprint and can have its own unique attributes and behaviors.
#inheritance - A mechanism by which a new class (derived class) can inherit attributes and
#and methods from an existing class (base class). This promotes code reusability and establishes a hierarchical relationship between classes.
#polymorphism - The ability of different classes to be treated as instances of the same class through a common interface. 
# It allows methods to do different things based on the object it is acting upon, even if they share the same name.

#function - A block of reusable code that performs a specific task. Functions can take inputs (parameters) and return outputs (results).
#method - A function that is defined within a class and is associated with the objects of that class. 
# Methods can operate on the object's data and perform actions related to the object.

#creating class
#class MyClass:
    #def Myfun(self):
        #pass          #this keyword will make python to skp this instance
    #def Myfun2(self, name):
        #print("Hello " + name)

#creating object
#obj = MyClass()
#obj.Myfun() 
#obj.Myfun2("Alice") #calling the method using object #object.methodname()

#we can create 2 methods. 1. static method 2. instance method
#1.static method - we can call only through object. 
#2.instance or class method - we can call through class name also by passing object as parameter

#example of instance method
#class MyClass:
    #def instance_method(self):
       # print("This is an instance method")
#creating object
#obj = MyClass()
#calling instance method using object
#obj.instance_method()
#calling instance method using class name by passing object as parameter
#MyClass.instance_method(obj)

#example of static method
#class MyClassStatic:
    #@staticmethod
    #def static_method(self, num):
        #print("This is a static method", num, self)
#creating object
#obj_static = MyClassStatic()
#calling static method using object
#obj_static.static_method(10, 20)
#calling static method using class name
#MyClassStatic.static_method()

#instance variable - variable that is defined inside a method and belongs to the instance of the class. This can be unique for each instance.
#class variable - variable that is defined inside a class but outside any method. This is shared among all instances of the class.
class Employee:
    num_of_emps = 0  #class variable
    raise_amount = 1.05  #class variable
    def __init__(self, first, last, pay):
        self.first = first  #instance variable
        self.last = last  #instance variable
        self.pay = pay  #instance variable
        self.email = first + '.' + last + '@company.com'  #instance variable
        Employee.num_of_emps += 1  #accessing class variable inside init method using class name. 
        #This will increase the count of employees whenever a new object is created.

    def fullname(self):
        return'{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  #using class variable inside instance method. we can acess through class(Employee) or instance(self)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount  #updating class variable using class method

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#emp1 = Employee('John', 'Doe', 50000)
#emp2 = Employee('Jane', 'Smith', 60000)

#Employee.set_raise_amount(1.08)  #calling class method using class name to update class variable

#print(emp1.fullname())  #calling instance method using object
#print(Employee.fullname(emp2))  #calling instance method using class name by passing object as parameter
#print("Total number of employees: ", Employee.num_of_emps) #accessing class variable using class name

#updating the class variable value
#Employee.raise_amount = 1.10 #updating class variable value through class name
#emp1.raise_amount = 1.10 #updating class variable value through object. this will create instance variable with same name

#to know the raise pecentage
#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)
#print(emp1.apply_raise())
#print(Employee.apply_raise(emp2))

#creating employee objects from string using class method
#emp_str_1 = 'Alice-Wonder-70000'
#emp_str_2 = 'Bob-Builder-80000'
#emp_str_3 = 'Charlie-Chaplin-90000'

#new_emp_1 = Employee.from_string(emp_str_1)
#new_emp_2 = Employee.from_string(emp_str_2)
#new_emp_3 = Employee.from_string(emp_str_3)
#print(new_emp_1.email)
#print(new_emp_2.pay)
#print(new_emp_3.fullname())

#regular methods pass instance as first parameter(self)
#class methods pass class as first parameter(cls)
#static methods don't pass anything automatically

#to check workday using static method
#import datetime
#my_date = datetime.date(2026, 1, 2)  #year, month, day
#print(Employee.is_workday(my_date))

#subclass or inherited class - A class that inherits attributes and methods from another class (base class).
#base class or parent class - The class from which attributes and methods are inherited.
class Developer(Employee):  #inheriting Employee class
    raise_amount = 1.10  #overriding class variable from parent class
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  #calling the init method of parent class using super()
        #or we can also use Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang  #adding new instance variable for subclass

dev1 = Developer('Dev', 'One', 70000, 'Python')
dev2 = Developer('Dev', 'Two', 80000, 'Java')
#print(dev1.pay)
#dev1.apply_raise()  #inherited method from parent class
#print(dev1.pay)

class Manager(Employee):  #inheriting Employee class
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

mgr1 = Manager('Manager', 'One', 90000, [dev1])
print(mgr1.email)
#mgr1.print_emps()
mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)
mgr1.print_emps()

#isinstance() - to check the object is instance of which class
#isfather() - to check the class is subclass of which class
#issubclass() - to check the class is subclass of which class
print(isinstance(mgr1, Manager))  #True
print(isinstance(mgr1, Employee))  #True
print(isinstance(mgr1, Developer))  #False
print(issubclass(Manager, Employee))  #True
print(issubclass(Developer, Employee))  #True
