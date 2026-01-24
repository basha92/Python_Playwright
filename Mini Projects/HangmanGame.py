#display different arts when user makes wrong guesses. End the game when user guesses the word or runs out of attempts.
import random
words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'developer', 'function', 'variable', 'condition']
#dictionary of key:(tuple) for no of wrong guesses and corresponding hangman art.
hangman_arts = {0:(" ", 
                   " ", 
                   " "),
                1:(" o ", 
                   "  ", 
                   "  "),
                2:(" o ", 
                   " |", 
                   "  "),
                3:(" o ", 
                   "/|", 
                   "  "),
                4:(" o ", 
                   "/|\\", 
                   "  "),
                5:(" o ", 
                   "/|\\", 
                   "/ "),
                6:(" o ", 
                   "/|\\", 
                   "/ \\")}
def display_man(wrong_guesses):  #display the lines based on the wrong guess
    for line in hangman_arts[wrong_guesses]:
        print(line)

def display_hint(hint): #display underscores and correct letters guessed so far
    print(" ".join(hint))  #joining the list into a string with space in between

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words) #selecting a random word from the list
    hint = ['_'] * len(answer) #creating a list of underscores for the hint which matches the length of the answer
    wrong_gusses = 0
    guessed_letters = set() #to keep track of letters already guessed
    max_wrong_guesses = 6
    is_running = True

    while is_running:
        display_man(wrong_gusses)
        display_hint(hint)
        print("\n")
        guess = input("Enter a letter: ").lower()

        #check the validity of the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.\n")
            continue
        #prompt if the letter has already been guessed
        if guess in guessed_letters:
            print(f"{guess} has already been guessed. Try a different letter.\n")
            continue
        
        guessed_letters.add(guess) #add the guess to the set of guessed letters

        #check whether the guess in the answer
        if guess in answer:
            for i in range(len(answer)): #iterate through the answer
                if answer[i] == guess: #if the letter matches the guess
                    hint[i] = guess #update the hint with the correct guess
        else:
            wrong_gusses += 1 #increment wrong guesses

        # check for win condition
        if '_' not in hint:
            print("Congratulations! You've guessed the word correctly!")
            display_man(wrong_gusses)
            display_answer(answer)
            is_running = False

        # check for lose condition
        if wrong_gusses >= max_wrong_guesses:
            print("Game over! You've run out of attempts.")
            display_man(wrong_gusses)
            print(f"The word was: {answer}")
            is_running = False



if __name__ == "__main__":
    main()