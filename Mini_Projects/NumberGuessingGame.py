'''
Requirement: guess between 10 to 100 randomly
loop the gamer until he guess and close once done. give how many tries
provide warnings for higher, lower and non integer inputs
'''

import random
min_number = 10
max_number = 100
guesses = 0
answer = random.randint(min_number, max_number)
is_running = True
print("Welcome to the guessing game!!")
print(f"select a number between {min_number} and {max_number}")
#taking input
while is_running:
        guess=input("Enter your guess: ")
        #1. check whether the input is number
        if guess.isdigit():
            guess = int(guess)
            guesses += 1
            if guess<min_number or guess>max_number:
                print("That number is out of range")
                print(f"Please select a number between {min_number} and {max_number}")
            elif guess > answer:
                print("Too High! Try Again!!")
            elif guess<answer:
                 print("Too Low! Try Again!!")
            else:
                 print("Correct Answer!")
                 print(f"Number of gusses: {guesses}")
                 is_running = False
        else:
            print("Invalid!")
            print(f"Enter a number between {min_number} and {max_number}")
'''
Output:

Welcome to the guessing game!!
select a number between 10 and 100
Enter your guess: 105
That number is out of range
Please select a number between 10 and 100
Enter your guess: 9
That number is out of range
Please select a number between 10 and 100
Enter your guess: dfgsdg
Invalid!
Enter a number between 10 and 100
Enter your guess: 23
Too Low! Try Again!!
Enter your guess: 56
Too Low! Try Again!!
Enter your guess: 89
Too High! Try Again!!
Enter your guess: 75
Too Low! Try Again!!
Enter your guess: 80
Too Low! Try Again!!
Enter your guess: 83
Too Low! Try Again!!
Enter your guess: 84
Too Low! Try Again!!
Enter your guess: 98
Too High! Try Again!!
Enter your guess: 95
Too High! Try Again!!
Enter your guess: 90
Too High! Try Again!!
Enter your guess: 88
Too High! Try Again!!
Enter your guess: 87
Correct Answer!
The answer is 87

TRY2:
Welcome to the guessing game!!
select a number between 10 and 100
Enter your guess: 23
Correct Answer!
Number of gusses: 1

'''
