import random

options = ("rock", "paper", "scissors")

is_running = True #helpful to break the loop after.

while is_running:
    player = None #player input initially. this will reset to none each time player starts to play
    computer = random.choice(options)
    #check whether user inputs correctly
    while player not in options:   #if player enters out of tuple, this will continue until getting from tuple.
        player = input("Enter your option (rock, paper, scissors): ")  #getting player status
    print(f"player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer=="scissors":
        print("You Win!")
    elif player == "scissors" and computer=="paper":
        print("You Win!")
    elif player == "paper" and computer=="rock":
        print("You Win!")
    else:
        print("You lose!")
    play_again = input("Want to play again? (Y/N): ").upper()
    if play_again == "N":
        is_running = False


print("Thanks foir playing!")

'''
output:
Enter your option (rock, paper, scissors): rock
player: rock
Computer: paper
You lose!
Want to play again? (Y/N): y
Enter your option (rock, paper, scissors): paper
player: paper
Computer: scissors
You lose!
Want to play again? (Y/N): y
Enter your option (rock, paper, scissors): scissors
player: scissors
Computer: paper
You Win!
Want to play again? (Y/N): n
Thanks foir playing!
'''