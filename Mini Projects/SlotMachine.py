#select randoem set of 3 symbols from a list of 5 symbols. If all 3 symbols match, user wins a payout based on the symbol.user can choose to quit anytime.

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols)for _ in range(3)]  #return any 3 random symbols using list comprehension. using _ as placeholder instead of a variable.

#beginner way to get the above output
    #result = []
    #for symbol in range(3):
        #result.append(random.choice(symbols))
    #return result

def print_row(row):
    print(" | ".join(row)) #joining the symbols with | in between.

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  #all 3 symbols are same 
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 5
        elif row[0] == '⭐':
            return bet * 10
    return 0  #no payout if no 3 symbols match  

def main():
    #required variables
    balance = 100

    #welcome message
    print("***********************")
    print("Welcome to Pythn Slots!")
    print("Symbols: 🍒🍉🍋🔔⭐")
    print("***********************")

    #taking the bet
    while balance>0:
        print(f"Your current balance is: ${balance: .2f}")

        bet = input("Enter your bet amount or 'q' to quit: ")
        if bet.lower() == 'q':
            break
        if not bet.isdigit():
            print("Invalid bet amount. Please enter a number.")
            continue
        if float(bet) > balance:
            print("Insufficient balance")
            continue
        if float(bet) <= 0:
            print("Bet amount must be greater than 0")
            continue
        bet = float(bet)
        balance -= bet
#calling the functions
#printing the spun row
        row = spin_row()
        print("spinning...")
        print_row(row)
#determining the payout
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout: .2f}")
        else:
            print("Sorry, you didn't win this time.")
        balance += payout
        play_again = input("Want to play again? (Y/N): ").upper()
        if play_again == "N":
            break

    print(f"Game over! Your final balance is: ${balance: .2f}")

if __name__ == "__main__":
    main()