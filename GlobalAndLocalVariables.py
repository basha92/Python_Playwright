#global variable - accessible throughout the entire module; defined outside of any function
#local variable - accessible only within the function where it is defined

# Global variable
#global_var = 100
#def demonstrate_variables():
    # Local variable
    #local_var = 50
    #print("Inside the function:")
    #print("Global Variable:", global_var)  # Accessing global variable
    #print("Local Variable:", local_var)    # Accessing local variable
#demonstrate_variables()
#print("Outside the function:")
#print("Global Variable:", global_var)  # Accessing global variable
# print("Local Variable:", local_var)    # This would raise an error, as local_var is not accessible outside the function

#xy = 100    # global variable
#def cool():
    #xy = 200    # local variable
    #print(xy)   # prints local variable
#cool()
#print(xy)       # prints global variable

#using global variable in local variable and update the value of global variable
#xy = 100    # global variable
#def cool():
    #global xy   # declare that we are using the global variable
    #xy = 200    # local variable
    #print(xy)   # prints local variable
#cool()
#print(xy)       # prints updated global variable

#defining global variable inside a function
def cool():
    global xy   # declare that we are using the global variable
    xy = 200    # updating global variable
    print(xy)   # prints updated global variable
cool()
print(xy)       # prints global variable