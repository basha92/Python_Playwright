#conditional statements
#if, if else
#Looping statements
#while, for
#Jumping statements
#break, continue

#conditional statements - print if a person is eligible to vote or not
#age=int(input("Enter your age: ")) #taking input from user
#if age>=18:
   # print("You are eligible to vote")
#else:
   # print("You are not eligible to vote")

#if else in single line (ternary operator)
#age=int(input("Enter your age: ")) #taking input from user
#print("You are eligible to vote") if age>=18 else print("You are not eligible to vote")

#multiple if else in single line (ternary operator)
#age=int(input("Enter your age: ")) #taking input from user
#print("You are a child") if age<18 else print("You are an adult") if age>=18 and age<60 else print("You are a senior citizen")

#Example:1
#num=int(input("Enter a number: ")) #taking input from user
#{print("hello"), print("python")} if num%2==0 else {print("hello"), print("java")}
#to print multiple statements in single line we use {}

#Example2: elif
#display the grade of a student based on the marks obtained
marks=int(input("Enter your marks: ")) #taking input from user
if marks>=90:
   print("A grade")
elif marks>=80:
    print("B grade")
elif marks>=70:
    print("C grade")
elif marks>=60:
    print("D grade")
elif marks>=50:
    print("E grade")
else:  
    print("F grade")
#nested if else
#num=int(input("Enter a number: ")) #taking input from user