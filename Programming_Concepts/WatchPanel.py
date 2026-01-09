#watch panel - the Watch panel is only visible during debugging. 
# It can be set to display the values of variables or arguments, 
# and values of user-defined expressions that are in scope. 
# These values are updated after each activity execution while debugging.
def calculate_average(grades: list):
    total_sum = 0
    total_numbers = len(grades)

    for numbers in grades:
        total_sum = numbers+total_sum

    return total_sum/total_numbers

def is_passed(avg):
    return avg>=40

grades = [50, 80, 90, 75, 68, 57, 41]

average = calculate_average(grades)
status = is_passed(average)

print(f"""Average: {average: .4f}
      Status: {status}""" )