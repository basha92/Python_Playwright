#we can pass 2 types of arguments to a function
#1. positional arguments
#2. keyword arguments
#def greet(name, message):
    ##print(f"{message}, {name}!")
#positional arguments
#greet("Alice", "Hello")
#greet("Bob", "Good morning")
#keyword arguments
#greet(message="Hi", name="Charlie")
#greet(name="Diana", message="Welcome")

#default value assigned to positional arguments
#def greet(name, message="Hello"):
    #print(f"{message}, {name}!")
#using default message
#greet("Eve") #Hello, Eve!
#greet with custom message
#greet("Frank", "Good evening") #Good evening, Frank! the passed value overrides the default value

#mixing positional and keyword arguments
#def greet(name, message="Hello"):
    #print(message + ", " + name + "!")
#greet("Grace")  # Uses default message
#greet("Heidi", "Good afternoon")  # Overrides default message
#greet(message="Hi there", name="Ivan")  # Keyword arguments can be in any order
#greet("Judy", message="Welcome aboard")  # Positional argument first, then keyword argument - thumb rule. If not followed, it may lead to error.
#greet(name="Karl", "Howdy")  # This will raise a SyntaxError because positional argument follows keyword argument
#greet("Liam", name="Howdy")  # logically error, but syntactically correct. - TypeError: greet() got multiple values for argument 'name'

#function that return multiple values
#def calculate(a, b):
    #sum = a + b
    #difference = a - b
    #product = a * b
    #return sum, difference, product
#result = calculate(10, 5) #returns a tuple
#print("Sum:", result[0])
#print("Difference:", result[1])
#print("Product:", result[2])
#we can also unpack the returned tuple into multiple variables
#sum, diff, prod = calculate(10, 5) #unpacking the returned tuple into multiple variables
#print("Sum:", sum)
#print("Difference:", diff)
#print("Product:", prod)

def largest(a,b):
    if (a >= b):
        return a , b
    else:
        return b , a
    
print(largest(10, 5))
print(largest(b=20, a=15))
