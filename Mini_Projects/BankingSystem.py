# to show basic operations like balance, withdraw, deposit and exit
def show_balance(balance):
    print("------------------------------")
    print(f"The balance is ${balance: .2f}")
    print("------------------------------")
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount<0:
        print("------------------------------")
        print("Amount must be greater than 0")
        print("------------------------------")
        return 0  # to avoid type errors
    elif amount>balance:
        print("------------------------------")
        print("Insufficient balance")
        print("------------------------------")
        return 0  # to avoid type errors
    elif amount == balance:
        return amount
    else:
        return amount
def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount<0:
        print("------------------------------")
        print("Amount must be greater than 0")
        print("------------------------------")
        return 0  #to avoid type errors
    else:
        return amount

def main():  #encapsulating for better readability. best practice.
    balance=0
    is_running=True

    while is_running:
        print(''' ******
        Banking Program
        1. Show Balance
        2. Make Withdraw
        3. Make Deposit
        4. Exit
        ******''')
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance -= withdraw(balance)
        elif choice == "3":
            balance += deposit()  #storing the balance amount after depositing.
        elif choice == "4":
            is_running=False
        else:
            print("This is not a valid choice")

    print("Thanks for banking with us!!")
if __name__=='__main__':   #its best practice to encapsulate the variables using this.
    main()
