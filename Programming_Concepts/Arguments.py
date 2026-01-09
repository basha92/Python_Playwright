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

#def largest(a,b):
    #if (a >= b):
        #return a , b
    #else:
        #return b , a
    
#print(largest(10, 5))
#print(largest(b=20, a=15))

#there are 4 types of arguments: 1. Positional 2.Functional 3.Keyword 4.Arbitary.
#Arbitary - we don't know how many non-key parameters will be passed to the function. *args will be used in that situation
#that will be in the form of tuple. To unpack * will be used.
#Keyword - allows you to pass multiple key parameters in the form of Dictionary. to unpack **kwargs will be used.

#example 1 of arbitary
#def add(*args):
    #total = 0
    #for arg in args:
        #total = total+arg
    #return total

#print(add(2,5,8, 10, 15))

#example 2 of arbitary
#def name(*args):
    #for arg in args:
        #print(f"{arg}\n", end=' ')

#name('Dr.', 'Sponge Bob', "Square", 'Pants')
#name('Monkey', "D.", 'Luffy')
#name('Zorro')
#name('One Piece')

#example of key word arguments - Dictionary is a key-value pair. So while passing and printing we need to do the same.
'''def display_address(**kwargs):
    for key, value in kwargs.items():    #accessing what is required in the dictionary. Key or value or item(both)
        print(f"{key}: {value}\n")

display_address(apt = '103', 
                building = 'Ramya Enclave', 
                street='Siddhi Vinayak Nagar', 
                area='Madhapur', 
                city='Hyderabad', 
                state='Telangana', 
                zip = '500081')


display_address(apt = '508', 
                building = 'Arunachala Apartments', 
                street='Siddhi Vinayak Nagar', 
                area='Madhapur', 
                city='Hyderabad', 
                state='Telangana', 
                zip = '500081')'''

#using *args and **kwargs in one place
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    #for value in kwargs.values():
        #print(value)
    if "apt" in kwargs and "pbno"in kwargs:    
        print(f"{kwargs.get('apt')}")
        print(f"{kwargs.get('pbno')} {kwargs.get('street')}")
    elif "apt" in kwargs:
        print(f"{kwargs.get('apt')}")
        print(f"{kwargs.get('street')}")
    elif "pbno" in kwargs:
        print(f"{kwargs.get('pbno')} {kwargs.get('street')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('state')} {kwargs.get('zip')}")

shipping_label('Dr.', 'Spongebob', 'Squarepants', 'III',
               apt = "568 Fake Building",
               pbno = '201',
               street = 'Fake Street',
               state = 'NY',
               zip = '0123')