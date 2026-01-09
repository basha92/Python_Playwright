#this file talks about the break points usage in debugging.
#Debugging in Software Engineering is the process of identifying and resolving 
#errors or bugs in a software system.
#breakpoint-it's a point where the program breaks/stops, 
# so you can use a debugger to inspect the internal state of the program. 
def sum_of_list(number_list: list):
    sum = 0
    for number in number_list:
        sum = sum+number
    return sum

#input for the list
input_numbers = [10, 20, 30, 40, 50]
result = sum_of_list(input_numbers)
print('sum is:', result)