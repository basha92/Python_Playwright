#this file contains basics about exception handling in python
#A return statement in a finally block overrides any return statement in the try or except blocks, 
# and it also swallows any exception that was in flight, preventing it from being raised. 
# This behavior is often unexpected and discouraged, as the finally block always executes before the function exits, 
# making its return the final one. 
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.") 
        return "Return from except"
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.") 
        return "Return from except"
    else:
        print("Result is:", result)
        return "Return from try"
    finally:
        print("Execution is complete.") 

# Example usage
#print(divide_numbers(10, 2))  # Should print 5.0
#print(divide_numbers(10, 0))  # Should print error message for division by zero
#print(divide_numbers(10, 'a'))  # Should print error message for invalid input type

#raising own exceptions
def enternumber(num):
    if num<0:
        raise ValueError("only integers")
    if num%2==0:
        print("even")
    else:
        print("odd")
print("checking the number is odd or even")
num = 5
try:
    enternumber(num)
except ValueError:
    print("value error occured and handled")

print("program completed")