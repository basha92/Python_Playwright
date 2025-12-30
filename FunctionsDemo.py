#function - a set of instructions/statements that perform a specific task. 
#It can take inputs, process them, and return an output and works when called.
#Defining a function - we need to do 2 tasks in function. 1. define the function 2. call the function
#Defining a function - use def keyword followed by function name and parentheses ().
#def greet():
    #print("Hello, welcome to the Functions Demo!")
#Calling the function - to execute the function, we need to call it by its name followed by parentheses.
#greet()

#Function with parameters
#def greet_user(name):
    #print(f"Hello, {name}! Welcome to the Functions Demo!")
#greet_user("Alice")
#greet_user("Bob")
#greet_user("Charlie")

#Function with return value
#def add_numbers(a, b):
    #return a + b
#result = add_numbers(5, 10)
#print(f"The sum of 5 and 10 is: {result}")

#none returning function - function that does not take any value and return any value
#def func():
   # return
   #i=10

#print(func())  # This will print 'None' since the function does not return any value

#function that does not take any value but returns a value
#def func():
    #i = 10
    #return i
#print(func()) #without print statement it will not show any output
# This will print '10' since the function returns the value of i; 
# since we are returning, need to use print statement or store in a variable to see the value

#function that takes values and does not return any value
#def func(a, b):
    #c = a + b
    #print(c)
#func(5, 10)  # This will print '15' since the function prints the sum of a and b

#function that takes values and returns a value
def func(a, b):
    c = a + b
    return c
result = func(5, 10)  # Storing the returned value in a variable
print(result)  # This will print '15' since the function returns the sum of a and b

