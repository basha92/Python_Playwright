#using dictionary

#food item list
menu = {"Pizza": 3.00,
        "Burger": 2.50,
        "French fry": 2.00,
        "Soda": 1.00,
        "Coke": 1.50,
        "Nuggets": 3.5}
cart = []
total = 0
#displaying menu
print("---------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------")

#getting order
while True:
    order = input("Enter the item(Q to quit):").capitalize()
    if order == "Q":
        break
    elif order in menu:
        cart.append(order)
#calculate total
print("---------ORDER----------")
for order in cart:
    total = total+menu.get(order)  #taking the associated value
    print(order, end="\n")
#print()
print(f"Total amount is: ${total}")
'''
Output:
---------MENU----------
Pizza     : $3.00
Burger    : $2.50
French fry: $2.00
Soda      : $1.00
Coke      : $1.50
Nuggets   : $3.50
-----------------------
Enter the item(Q to quit):pizza
Enter the item(Q to quit):burger
Enter the item(Q to quit):q
---------ORDER----------
Pizza
Burger
Total amount is: $5.5
'''