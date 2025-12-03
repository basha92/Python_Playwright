#storing string in a variable
#greeting = "Hello, World!"
#greeting_single = 'Hello, World!'
#greeting_triple = """Hello, World!"""
#greeting_triple_single = '''Hello, World!'''   
#greeting_multiline = """Hello,
#World!"""  
#print(greeting)
#print(greeting_single)
#print(greeting_triple)
#print(greeting_triple_single)
#print(greeting_multiline)

#storing string using str() function
#number_str = str("12345")
#print(number_str)
#number_str_single = str('12345')
#print(number_str_single)

#creating empty string
#empty_str = ""
#empty_str_single = ''

#string operations
#mutable - can change the value of the variable
#immutable - cannot change the value of the variable
#strings are immutable in python

#printing string id
#str1 = "Hello"
#print("String 1 ID:", id(str1)) #2418150714768 - this is the memory address of the string
#str1 += ", World!"  #modifying the string
#print("Modified String 1:", str1)
#print("Modified String 1 ID:", id(str1)) #2641285102640 - new memory address after modification
#if the id changes, the string is immutable

#using + and * operators with strings
#tr2 = "Hello"
#str3 = "World"
#concatenated_str = str2 + ", " + str3 + "!"
#print("Concatenated String:", concatenated_str)  #Hello, World!
#repeated_str = str2 * 3    #this will repeat the string 3 times
#print("Repeated String:", repeated_str)  #HelloHelloHello

#string indexing and slicing
sample_str = "Hello, World!"
print("Original String:", sample_str)
print("First Character:", sample_str[0])  #H
print("Last Character:", sample_str[-1])  #!
print("Substring (0-5):", sample_str[0:5])  #Hello
print("Substring (7-12):", sample_str[7:12])  #World
print("Substring (::2):", sample_str[::2])  #Hlo ol!