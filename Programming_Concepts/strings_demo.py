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
#sample_str = "Hello, World!"
#print("Original String:", sample_str)
#print("First Character:", sample_str[0])  #H
#print("Last Character:", sample_str[-1])  #!
#print("Substring (0-5):", sample_str[0:5])  #Hello
#print("Substring (7-12):", sample_str[7:12])  #World
#print("Substring (::2):", sample_str[::2])  #Hlo ol!

#ord() and chr() functions  
#char = 'A'
#print("Character:", char)
#print("ASCII Value using ord():", ord(char))  #65 - ASCII value of 'A'

#string length  
#sample_str = "Hello, World!"
#print("String:", sample_str)
#print("Length of String using len():", len(sample_str))  #13 - length of the string
#print("last letter of the string using max():", max(sample_str))  #w - last letter in alphabetical order, retruns W as it has the highest ASCII value
#print("first letter of the string using min():", min(sample_str))  # , - first letter in alphabetical order, returns space as it has the lowest ASCII value
#max and min functions return the character with the highest and lowest ASCII values respectively

#in, not in operators - returns True or False based on conditions
#sample_str = "Hello, World!"
#print("Is 'World' in the string?", 'World' in sample_str)  #True
#print("Is 'Python' in the string?", 'Python' in sample_str)  #False
#print("Is 'World' not in the string?", 'World' not in sample_str)  #False
#print("Is 'Python' not in the string?", 'Python' not in sample_str)  #True

#string comparison - compares the strings lexicographically based on ASCII values and returns True or False
#str_a = "apple"
#str_b = "banana"
#print("String A:", str_a)
#print("String B:", str_b)
#print("Is String A equal to String B?", str_a == str_b)  #False
#print("Is String A not equal to String B?", str_a != str_b)  #True
#print("Is String A less than String B?", str_a < str_b)  #True
#print("Is String A greater than String B?", str_a > str_b)  #False
#print("Is String A less than or equal to String B?", str_a <= str_b)  #True
#print("Is String A greater than or equal to String B?", str_a >= str_b)  #False
#comparison is done based on the ASCII values of the characters in the strings

#testing strings true or false
#s = "welcome to python"
#print(s.isalnum())  #False - contains spaces
#print("welcome".isalpha())  #True - only alphabets
#print("welcome123".isalnum())  #True - contains only alphabets and numbers  
#print("12345".isdecimal())  #True - contains only numbers
#print("   ".isspace())  #True - contains only spaces
#print("WELCOME".isupper())  #True - all uppercase letters
#print("welcome".islower())  #True - all lowercase letters
#print("Welcome".istitle())  #True - first letter is uppercase and rest are lowercase
#print("first number".isidentifier())  #False - contains space

#finding substrings
#sample_str = "Hello, welcome to the world of Python programming. Python is great!"
#first_index = sample_str.find("Python")  #finds the first occurrence of the substring
#print("First occurrence of 'Python' is at index:", first_index)  #39
#print(sample_str.find("Java"))  #-1 - substring not found
#print(sample_str.endswith("great!"))  #True - checks if the string ends with the specified substring
#print(sample_str.startswith("Hello"))  #True - checks if the string starts with the specified substring
#print(sample_str.count("Python"))  #2 - counts the occurrences of the substring

#string conversion methods
#sample_str = "  hello, welcome to python programming  "
#print("Original String:", repr(sample_str))
#print("Uppercase:", sample_str.upper())  #HELLO, WELCOME TO PYTHON PROGRAMMING
#print("Lowercase:", sample_str.lower())  #hello, welcome to python programming
#print("Title Case:", sample_str.title())  #Hello, Welcome To Python Programming
#print("Capitalized:", sample_str.capitalize())  #Hello, welcome to python programming
#print("Stripped String:", repr(sample_str.strip()))  #hello, welcome to python programming
#print("Replaced String:", sample_str.replace("python", "Java"))  #  hello, welcome to Java programming
#print("Split String:", sample_str.split())  #['hello,', 'welcome', 'to', 'python', 'programming']

#string reversal - interview question
#method 1: using for loop
sample_str = "Hello, World!"
reversed_str = ""
for char in sample_str:
    reversed_str = char + reversed_str
print("Reversed String using for loop:", reversed_str)  #!dlroW ,olleH

#method 2: using slicing
reversed_str_slicing = sample_str[::-1]  #[start:stop:step] - step of -1 means to go backwards
print("Reversed String using slicing:", reversed_str_slicing)  #!dlroW ,olleH
